# Importing Django Libraries required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login
from django.template.loader import render_to_string
from django.utils import timezone
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.core.mail import EmailMessage
from django.contrib.auth.models import update_last_login

from Register_Login.exception import APIException
from Register_Login.models import Profile
from .schema import get_all_users_schema,get_user_by_email_Schema,create_user_schema

# GraphQL Libraries
from graphene_django.views import GraphQLView
from django.http import JsonResponse

# Importing the utilts file
from Register_Login.utils import AccessTokenGenerator



# Rest Libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Register_Login.serializers import LoginSerializer, UserSerializer
from django.http import JsonResponse



# Creating Users
@csrf_exempt 
@api_view(['GET','POST'])
def create_users_API(request):
    if request.method == 'GET':
        all = Profile.objects.filter(is_active = True)
        serializer = UserSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)

    if request.method == 'POST':
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
            return Response("Serializer Not Valid", status = status.HTTP_400_BAD_REQUEST)

# Login Users
@csrf_protect
@api_view(['GET','POST','PUT'])
def login_users_API(request):
    if request.method == 'GET':
        all = Profile.objects.filter(is_active = True)
        serializer = LoginSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = LoginSerializer(data= request.data,context={'request': request})
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            print("Valid")
            user = authenticate(request, email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
            )
            if user:
                if user.is_active:
                        update_last_login(None, user)
                        user_login(request, user)
                        print('active')
                        print(HttpResponse.status_code)
                        return Response(status = status.HTTP_302_FOUND)

                else:
                    print('Not Active')
                    return Response.status_code
           
            else:
                print('Invalid Credentials')
                print(status.HTTP_404_NOT_FOUND)
                return Response(status = status.HTTP_404_NOT_FOUND)
                
        else:
            print("Not Valid")
        return Response(serializer.data, status = status.HTTP_404_NOT_FOUND)
    





@csrf_exempt
def graphql(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_all_users_schema, graphiql=True))(request)

@csrf_exempt
def Usergraphql(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_user_by_email_Schema, graphiql=True))(request)
@csrf_exempt
def signUpGraph(request):
    return csrf_exempt(GraphQLView.as_view(schema=create_user_schema, graphiql=True))(request)



