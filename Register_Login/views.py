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
from django.http import JsonResponse


# Importing the utilts file
from rest_framework import generics

from .schema import get_all_users_schema

# Rest Libraries
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Register_Login.serializers import ChangePasswordSerializer, LoginSerializer, UserSerializer, updateLimitSerializer
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import APIException, AuthenticationFailed
from django.utils.decorators import method_decorator

from twilio.rest import Client

def SendSms(request,user):
        print(user.PhoneNumber)    
        account_sid = 'AC7cf95e0405320e10ea82909a44799314'
        auth_token = '8e37eece365e2baf9803659c35d314a0'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+13184077006',
            body=f"Hi {user.first_name} Please insert this Code {user.otp}",
            to=str(user.PhoneNumber)
            )
        print(message.sid)
        return JsonResponse({"Status": "Success"}, safe=False,status = status.HTTP_200_OK)



# @method_decorator(csrf_exempt, name='dispatch')
class RegisterAPIView(APIView):
    def post(self,request):
        serializer = UserSerializer(data= request.data,partial=True)
        if Profile.objects.filter(PhoneNumber=request.data['PhoneNumber']).exists():
            return Response("PhoneNumber Exist, Please Login", status = status.HTTP_400_BAD_REQUEST)
        else:
            user = Profile.objects.create_user(
                        email=request.data['email'],
                        first_name=request.data['first_name'],
                        last_name=request.data['last_name'],
                        password=request.data['password'],
                        city=request.data['city'],
                        PhoneNumber=request.data['PhoneNumber'],
                        is_active = False
                    )
            if user:
                SendSms(request,user)
                return Response("User Created Successfully, Sms has been sent", status = status.HTTP_200_OK)
            else:
                return Response("Error Creating User", status = status.HTTP_400_BAD_REQUEST)



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
    
    

class updateLimitAPI(APIView):
    def post(self, request,email):
        serializer = updateLimitSerializer(data=request.data)
        if request.data != None:
            user = Profile.objects.get(email=email)
            if user.allow_download == True:
                if user.download_limit == 0:
                     return Response("User Download Limit equals 0", status=status.HTTP_400_BAD_REQUEST)
                else:
                    limit = user.download_limit - 1
                    Profile.objects.filter(email=email).update(download_limit=limit)
                    print(user.download_limit)
                    return Response(limit, status=status.HTTP_200_OK)
            else:
                return Response("User Allow Download field in Database is False", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Data is Not Valid", status=status.HTTP_400_BAD_REQUEST)


    def get(self,request,email):
        all = Profile.objects.filter(email=email)
        serializer = updateLimitSerializer(all, many=True)
        return JsonResponse({"Names": serializer.data}, safe=False) 


@csrf_exempt
def getUsers(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_all_users_schema, graphiql=True))(request)


class GetUserByeEmail(APIView):
    def post(self,request):
        serializer = UserSerializer(data= request.data)
        pass
        
    def get(self, request,email):
        all = Profile.objects.filter(email=email)
        serializer = UserSerializer(all, many = True)
        return JsonResponse({"Names": serializer.data}, safe=False,status = status.HTTP_200_OK)
    


class ResendCode(APIView):
    def post(self, request,email):
        user = Profile.objects.get(email= email)
        print(user.PhoneNumber)    
        account_sid = 'AC7cf95e0405320e10ea82909a44799314'
        auth_token = '9aa8515feaa56bd3abd41b9369f06d93'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                from_='+13184077006',
                body=f"Hi {user.first_name} Please insert this Code {user.otp}",
                to=str(user.PhoneNumber)
                )
        print(message.sid)
        return JsonResponse({"Status": "Success"}, safe=False,status = status.HTTP_200_OK)


class check_otp(APIView):
    def post(self,request,email,otp):
        user = Profile.objects.get(email=email)
        if user.is_active == False and otp == None:
            return JsonResponse({"Status": "Otp is Empty"}, safe=False,status = status.HTTP_400_BAD_REQUEST)
        elif user.is_active == False and otp == user.otp:
            Profile.objects.filter(email=email).update(is_active=True)
            return JsonResponse({"Status": "user activated"}, safe=False,status = status.HTTP_200_OK)
        elif user.is_active == True and otp == user.otp:
            return JsonResponse({"Status": "The User Already Active and Authenticated"}, safe=False,status = status.HTTP_400_BAD_REQUEST)
        elif otp != user.otp:
            return JsonResponse({"Status": "The otp is Wrong"}, safe=False,status = status.HTTP_400_BAD_REQUEST)
