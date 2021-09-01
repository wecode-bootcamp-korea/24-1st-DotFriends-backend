import json
import re
import bcrypt
import jwt

from django.http import JsonResponse
from django.views import View

from users.models import User
from my_settings import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email          = data['email']
            password       = data['password']
            address        = data['address']
            nickname       = data['nickname']
            ck_password    = data['ck_password']
            phone_number   = data['phone_number']
            Valid_password = re.compile('^(?=.*[a-zA-Z])(?=.*[\d])(?=.*[~!@#$%^&*_+])[a-zA-Z\d~!@#$%^&*_+]{8,}$')
            Valid_email    = re.compile('^[a-zA-Z\d+-_.]+@[a-zA-Z\d]+\.[a-zA-Z\d+-.]+$')

            if not Valid_email.match(email):
                return JsonResponse({'MESSAGE':'EMAIL_VALIDATION'}, status=400)

            if not Valid_password.match(password):
                return JsonResponse({'MESSAGE':'PASSWORD_VALIDATION'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE':'ALREADY_EXISTED_EAMil'}, status=400)

            if not password == ck_password:
                return JsonResponse({'MESSAGE':'PASSWORD_NOT_CORRECT'}, status=400)
            
            hashed_password  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                nickname     = nickname,
                email        = email,
                password     = hashed_password,
                address      = address,
                phone_number = phone_number,
            )

            return JsonResponse({'MESSAGE':'CREATE'}, satuts=201)
        
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'MESSAGE':'VALUE_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if User.objects.filter(email=data['email']).exists():

                if bcrypt.checkpw(data['password'].encode('utf-8'), User.objects.get(email=data['email']).password.encode('uft-8')):
                    token = jwt.encode({'id' : User.objects.get(email=data['email']).id},SECRET_KEY, algorithm='HS256')
                    return JsonResponse({'MESSAGE':'SUCCESS', 'TOKEN' : token}, status=200)
            
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)