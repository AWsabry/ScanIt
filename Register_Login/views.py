# Importing Django Libraries required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.translation import gettext as _
from django.core.mail import EmailMessage
from rest_framework.permissions import IsAuthenticated   
from graphene_django.views import GraphQLView

from Register_Login.authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token

from Register_Login.exception import APIException
from Register_Login.models import Profile


# Importing the utilts file
from rest_framework import generics

from .schema import get_all_users_schema

# Rest Libraries
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Register_Login.serializers import ChangePasswordSerializer, LoginSerializer, UserSerializer
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



class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = Profile
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    




# @csrf_exempt
# def graphql(request):
#     return csrf_exempt(GraphQLView.as_view(schema=get_all_users_schema, graphiql=True))(request)

# @csrf_exempt
# def Usergraphql(request):
#     return csrf_exempt(GraphQLView.as_view(schema=get_user_by_email_Schema, graphiql=True))(request)
# @csrf_exempt
# def signUpGraph(request):
#     return csrf_exempt(GraphQLView.as_view(schema=create_user_schema, graphiql=True))(request)



@csrf_exempt
def getUsers(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_all_users_schema, graphiql=True))(request)