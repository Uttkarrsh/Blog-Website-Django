from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def log(request):
    return render(request, 'home.html')

class LoginView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key Username not found'
                raise Exception('key Username not found')

            if data.get('password') is None:
                response['message'] = 'key Password not found'
                raise Exception('key Password not found')

            checkUser = User.objects.filter(username = data.get('username')).first()

            if checkUser is None:
                response['message'] = 'Invalid Username, user not found' 
                raise Exception('Invalid Username not Found')
            
            user_obj = authenticate(username = data.get('username'), password = data.get('password'))
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = "Welcome"
            else:
                response['message'] = 'Invalid password' 
                raise Exception('Invalid password')

        
        except Exception as e:
            print(e)
    
        return Response(response)

LoginView = LoginView.as_view()


class RegisterView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key Username not found'
                raise Exception('key Username not found')
            if data.get('username') == '':
                response['message'] = 'key Username not found'
                raise Exception('key Username not found')

            if data.get('password') is None:
                response['message'] = 'key Password not found'
                raise Exception('key Password not found')
            if data.get('password') == '':
                response['message'] = 'key Password not found'
                raise Exception('key Password not found')

            checkUser = User.objects.filter(username = data.get('username')).first()

            if checkUser:
                response['message'] = 'Username already exists' 
                raise Exception('username alreadytaken')
            
            user_obj = User.objects.create(username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['status'] = 200
            response['message'] = 'User Created'

        
        except Exception as e:
            print(e)
    
        return Response(response)

RegisterView = RegisterView.as_view()