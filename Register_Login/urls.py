from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import RegisterAPIView, LoginAPIView, UserAPIView, RefreshAPIView, LogoutAPIView,ChangePasswordView,updateLimitAPI, getUsers,GetUserByeEmail,ResendCode,check_otp


app_name = 'Register_Login'

urlpatterns = [



    path('register/', view =RegisterAPIView.as_view(),),

    path('login/', view = LoginAPIView.as_view(),), # this will return token
    path('user', view =UserAPIView.as_view(),), # will return user data
    path('refresh', view =RefreshAPIView.as_view(),), # expecting to refresh the token
    path('logout', view =LogoutAPIView.as_view(),),  # kill the refresh token
    path('ChangePasswordView', view =ChangePasswordView.as_view(),),  # kill the refresh token
    path('update_limit/<str:email>', updateLimitAPI.as_view(),), # Update Download Limit




    # path('signUp/', view= signUp, name='signUp'),
    # path('login/', view= login, name='login'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('graphql/',view = graphql, name = "graphql"),
    # path('createuserg/',view=signUpGraph, name= "signUpGraph"),
    path('getUsers/',view = getUsers, name = "getUsers"),
    path('get_user_by_email/<str:email>',view = GetUserByeEmail.as_view(), name = "get_user_by_email"),
    path('checkotp/<str:email>/<str:otp>/',view = check_otp.as_view(), name = "checkotp"),
    path('resendCode/<str:email>/',view = ResendCode.as_view(), name = "resendcode"),
    

    # Graphql Paths
]



