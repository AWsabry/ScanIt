from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import RegisterAPIView, LoginAPIView, UserAPIView, RefreshAPIView, LogoutAPIView,ChangePasswordView,updateLimitAPI, getUsers,GetUserByeEmail,ResendCode,check_otp,ContactUsView,update_daily_limit


app_name = 'Register_Login'

urlpatterns = [



    path('register/', view =RegisterAPIView.as_view(),),

    path('login/', view = LoginAPIView.as_view(),), # this will return token
    path('user', view =UserAPIView.as_view(),), # will return user data
    path('refresh', view =RefreshAPIView.as_view(),), # expecting to refresh the token
    path('logout', view =LogoutAPIView.as_view(),),  # kill the refresh token
    path('ChangePasswordView', view =ChangePasswordView.as_view(),),  # kill the refresh token
    path('update_limit/<str:email>', updateLimitAPI.as_view(),), # Update Download Limit
    path('getUsers/',view = getUsers, name = "getUsers"),
    path('get_user_by_email/<str:email>',view = GetUserByeEmail.as_view(), name = "get_user_by_email"),
    path('checkotp/<str:email>/<str:otp>/',view = check_otp.as_view(), name = "checkotp"),
    path('resendCode/<str:email>/',view = ResendCode.as_view(), name = "resendcode"),
    path('contactUs/',view = ContactUsView.as_view(), name = "contactUs"),
    path('update_daily_limit/<str:email>',view = update_daily_limit.as_view(), name = "update_daily_limit"),

    # Graphql Paths
]



