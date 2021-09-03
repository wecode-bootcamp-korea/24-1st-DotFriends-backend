from django.http.response import HttpResponse

def input_validator(func):
    def wraper(self, request, *args, **kwargs):
        try:
            offset = int(request.GET.get('offset', 1))
            limit  = int(request.GET.get('limit', 12))
            order  = request.GET.get('order', 'id')
            if not (order == 'id' or order == '-id' or order == '?' ):
                return HttpResponse(status=400) 
        except ValueError:
            return HttpResponse(status=400) 
        return func(self, request, *args, **kwargs)
    return wraper

            

    