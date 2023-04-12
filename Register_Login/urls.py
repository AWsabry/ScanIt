from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from Register_Login.views import graphql,Usergraphql,signUpGraph, create_users_API, login_users_API


app_name = 'Register_Login'

urlpatterns = [


    path('create_users_API/', view= create_users_API, name='create_users_API'),
    path('login_users_API/', view= login_users_API, name='login_users_API'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    # Graphql Paths
    path('graphql/',view = graphql, name = "graphql"),
    path('createuserg/',view=signUpGraph, name= "signUpGraph"),
    path('usergraph/',view = Usergraphql, name = "Usergraphql"),
]



