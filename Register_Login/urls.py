from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from Register_Login.views import graphql,Usergraphql,signUpGraph, signUp, login


app_name = 'Register_Login'

urlpatterns = [


    path('signUp/', view= signUp, name='signUp'),
    path('login/', view= login, name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    # Graphql Paths
    path('graphql/',view = graphql, name = "graphql"),
    path('createuserg/',view=signUpGraph, name= "signUpGraph"),
    path('usergraph/',view = Usergraphql, name = "Usergraphql"),
]



