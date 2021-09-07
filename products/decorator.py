from products.models import Category
from django.http.response import HttpResponse
from django.conf import settings
import jwt

def input_validator(func):
    def wraper(self, request, *args, **kwargs):
        try:
            offset = int(request.GET.get('offset', 0))
            limit  = int(request.GET.get('limit', 0))
            order  = request.GET.get('order', 'id')
            if not (order == 'id' or order == '-id' or order == '?' ):
                return HttpResponse(status=400) 
        except ValueError:
            return HttpResponse(status=400) 
        return func(self, request, *args, **kwargs)
    return wraper

def visitor_validator(func):
    def wraper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization',None)
            if not access_token:
                request.user = None
                return func(self, request, *args, **kwargs)
            token = jwt.decode(access_token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=token['id'])
            request.user = user
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'},status=401)
        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE':'INVALID_TOKEN'},status=401)
        return func(self, request, *args, **kwargs)
    return wraper
