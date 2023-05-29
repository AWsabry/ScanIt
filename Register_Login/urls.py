from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import RegisterAPIView, LoginAPIView, UserAPIView, RefreshAPIView, LogoutAPIView,ChangePasswordView, getUsers


app_name = 'Register_Login'

urlpatterns = [



    path('register/', view =RegisterAPIView.as_view(),),

    path('login/', view = LoginAPIView.as_view(),), # this will return token
    path('user', view =UserAPIView.as_view(),), # will return user data
    path('refresh', view =RefreshAPIView.as_view(),), # expecting to refresh the token
    path('logout', view =LogoutAPIView.as_view(),),  #kill the refresh token
    path('change-password/', ChangePasswordView.as_view(),), #Change Password




    # path('signUp/', view= signUp, name='signUp'),
    # path('login/', view= login, name='login'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('graphql/',view = graphql, name = "graphql"),
    # path('createuserg/',view=signUpGraph, name= "signUpGraph"),
    path('getUsers/',view = getUsers, name = "getUsers"),


    # Graphql Paths
]



