# Importing Django Libraries required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login, logout

from django.template.loader import render_to_string
from django.utils import timezone
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.core.mail import EmailMessage
from django.contrib.auth.models import update_last_login


from Register_Login.authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token

from Register_Login.exception import APIException
from Register_Login.models import Profile
from .schema import get_all_users_schema,get_user_by_email_Schema,create_user_schema

# GraphQL Libraries
from graphene_django.views import GraphQLView
from django.http import JsonResponse

# Importing the utilts file
from Register_Login.utils import AccessTokenGenerator



# Rest Libraries
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Register_Login.serializers import LoginSerializer, UserSerializer
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import APIException, AuthenticationFailed
from django.utils.decorators import method_decorator


# @method_decorator(csrf_exempt, name='dispatch')
class RegisterAPIView(APIView):
    def post(self,request):
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            user = Profile.objects.create_user(
                    email=request.data['email'],
                    first_name=request.data['first_name'],
                    last_name=request.data['last_name'],
                    password=request.data['password'],
                    city=serializer.validated_data['city'],
                    PhoneNumber=request.data['PhoneNumber'],
                    is_active = True
                )
            if user:
                return Response("User Created Successfully", status = status.HTTP_200_OK)
            else:
                return Response("Error Creating User", status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Serializer Not Valid, Check Your Data Inputs", status = status.HTTP_400_BAD_REQUEST)


# @method_decorator(csrf_exempt, name='dispatch')
class LoginAPIView(APIView):
    def post(self, request):
        user = Profile.objects.filter(email=request.data['email']).first()
        if not user:
            raise APIException('Invalid credentials!')

        if not user.check_password(request.data['password']):
            raise APIException('Invalid credentials!')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()
        response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)

        response.data = {
            'token': access_token
        }
        return response


class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = Profile.objects.filter(pk=id).first()

            return Response(UserSerializer(user).data)

        raise AuthenticationFailed('unauthenticated')
    
class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')

        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({
            'token': access_token
        })
    
    
class LogoutAPIView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie(key="refreshToken")
        logout(request)
        response.data = {
            'message': 'success'
        }
        return response
    

# Login Users
# @csrf_exempt 
# @api_view(['GET','POST','PUT'])
# def login(request,token):
#     if request.method == 'GET':
#         all = Profile.objects.filter(is_active = True)
#         serializer = LoginSerializer(all,many = True)
#         return JsonResponse({"Names": serializer.data}, safe=False)

#     if request.method == 'POST':
#         serializer = LoginSerializer(data= request.data,context={'request': request},)
#         print(serializer)
#         if serializer.is_valid(raise_exception=True):
#             print("Valid")
#             user = authenticate(request, email=serializer.validated_data['email'],
#             password=serializer.validated_data['password'],)
#             if user:
#                 if user.is_active:
#                         update_last_login(None, user)
#                         user_login(request, user)
#                         print('active')
#                         print(HttpResponse.status_code)
#                         return Response("User Logged In Successfully", status = status.HTTP_200_OK)

#                 else:
#                     print('Not Active')
#                     return Response("User is Not Active", status = status.HTTP_400_BAD_REQUEST)
           
#             else:
#                 print('Invalid Credentials')
#                 print(status.HTTP_400_BAD_REQUEST)
#                 return Response("Invalid Credentials", status = status.HTTP_400_BAD_REQUEST)
                
#         else:
#             print("Not Valid")
#         return Response(serializer.data, status = status.HTTP_404_NOT_FOUND)


# Creating Users
# @csrf_exempt 
# @api_view(['GET','POST'])
# def signUp(request):
#     if request.method == 'GET':
#         all = Profile.objects.filter(is_active = True)
#         serializer = UserSerializer(all,many = True)
#         return JsonResponse({"Names": serializer.data}, safe=False)

#     if request.method == 'POST':
        # serializer = UserSerializer(data= request.data)
        # if serializer.is_valid():
        #     user = Profile.objects.create_user(
        #             email=request.data['email'],
        #             first_name=request.data['first_name'],
        #             last_name=request.data['last_name'],
        #             password=request.data['password'],
        #             city=serializer.validated_data['city'],
        #             PhoneNumber=request.data['PhoneNumber'],
        #             is_active = True
        #         )
        #     if user:
        #         return Response("User Created Successfully", status = status.HTTP_200_OK)
        #     else:
        #         return Response("Error Creating User", status = status.HTTP_400_BAD_REQUEST)
        # else:
        #     return Response("Serializer Not Valid", status = status.HTTP_400_BAD_REQUEST)
    




# @csrf_exempt
# def graphql(request):
#     return csrf_exempt(GraphQLView.as_view(schema=get_all_users_schema, graphiql=True))(request)

# @csrf_exempt
# def Usergraphql(request):
#     return csrf_exempt(GraphQLView.as_view(schema=get_user_by_email_Schema, graphiql=True))(request)
# @csrf_exempt
# def signUpGraph(request):
#     return csrf_exempt(GraphQLView.as_view(schema=create_user_schema, graphiql=True))(request)



