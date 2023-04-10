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
from .schema import get_all_users_schema,get_user_by_email_Schema,create_user_schema

# GraphQL Libraries
from graphene_django.views import GraphQLView
from django.http import JsonResponse

# Importing the utilts file
from Register_Login.utils import AccessTokenGenerator

# Importing setting from the main project
from scanit import settings


# Importing Models
from Register_Login.models import AccessToken, Profile, Team_Member


# Importing Forms
from Register_Login.forms import LoginForm, RegisterForm

# Firebase Libraries
from django.http import QueryDict

# Email Confirm SignUp
def send_tracking(user):
    user = Profile.objects.filter(id=user.id).first()
    last_token = user.token.filter(user=user, expires__gt=timezone.now()).first()
    if not last_token:
        access_token = user.token.create(user=user)
        return (access_token.token, 0)
    return (False, (last_token.expires - timezone.now()).total_seconds())


# Checking the token availablity & creating the cart


def token_check(user):
    token, time_tosend = send_tracking(user=user)
    if token:
        return (token, time_tosend)
    return (None, time_tosend)


def send_activate_mail(request, user):
    token, time_tosend = token_check(user)
    if token:
        domain = get_current_site(request)
        subject = _("Activate user account")
        body = render_to_string(
            "activate.html",
            {
                "user": user,
                "domain": domain,
                "token": token,
            },
        )
        email = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [user.email])
        email.send()

        messages.success(request, _("Kindly check your inbox & junk for confirmation,"))
    else:
        messages.error(
            request,
            _(
                "Please varify the account (an email have been sent) please wait %(time_tosend)8.0f"
            )
            % {"time_tosend": time_tosend},
            extra_tags="danger",
        )


# This function is to create a new user profile & be saved in the models
@csrf_exempt
def Register(request):
    if request.user.is_authenticated:
        return redirect("categories_and_products:index")
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            email = form.data.get("email")
            first_name, last_name, school, nu_id = (
                form.data.get("first_name"),
                form.data.get("last_name"),
                form.data.get("school"),
                form.data.get("nu_id"),
            )
            password, password2 = form.data.get("password1"), form.data.get("password2")
            title, PhoneNumber = (
                form.data.get("title"),
                form.data.get("PhoneNumber"),
            )

            if Profile.objects.filter(email=email).exists():
                messages.error(request, "This Email Exists !")

            elif password != password2:
                messages.error(request, "Password does not matches")

            else:
                user = Profile.objects.create_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                    nu_id=nu_id,
                    school=school,
                    title=title,
                    PhoneNumber=PhoneNumber,
                )
                send_activate_mail(request, user)
                if not user:
                    messages.error(request, "Your email is not active")
                else:
                    pass
                return redirect("Register_Login:email_sent")
        else:
            form = RegisterForm()
        return render(request, "Register.html", {})


# Confirming sending email to user
def email_sent(request):
    return render(request, "email_sent.html")


def password_reset_emailing(request):
    return render(request, "registration/password_reset_completing.html")


# Logout Page


def activate_user(request, token):
    token = AccessToken.objects.filter(token=token).first()

    if token:
        last_token = AccessToken.objects.filter(
            user=token.user, expires__gt=timezone.now()
        ).first()

        if last_token == token:

            if AccessTokenGenerator().check_token(token.user, token.token):
                token.user.is_active = True
                token.user.save()
                messages.success(request, "Your account has been activated")
                return redirect("Register_Login:email_activated")
            return HttpResponse("already activated")
        return HttpResponse("timeout")

    return HttpResponse("None found token")


def logOut(request):
    logout(request)
    return render(
        request,
        "LogOut.html",
    )


def email_activated(request):
    return render(
        request,
        "email_activated.html",
    )


def index(request):
    return render(request, "index.html",)


def team(request):
    team_member = Team_Member.objects.filter(is_active=True)
    context = {"team_member": team_member}
    return render(request, "team.html", context)


# Login View
def signIn(request):
    form = LoginForm(request.POST, request.FILES)
    if request.user.is_authenticated:
        return redirect("categories_and_products:index")
    else:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, email=email, password=password)
            if form.is_valid():
                if user.is_active:
                    user_login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    messages.error(
                        request,
                        "Your account is not active, Please Register with valid Email",
                    )
            else:
                messages.error(
                    request,
                    "Please Login with your right Credentials and check your email for activation",
                )

        return render(request, "login.html", {"form": form})


def about_us(request):
    return render(
        request,
        "about_us.html",
    )


def profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(email=request.user)
        context = {

        }
    else:
        return redirect("Register_Login:login")
    return render(request, "profile.html", context)
    



@csrf_exempt
def graphql(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_all_users_schema, graphiql=True))(request)

@csrf_exempt
def Usergraphql(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_user_by_email_Schema, graphiql=True))(request)
@csrf_exempt
def signUpGraph(request):
    return csrf_exempt(GraphQLView.as_view(schema=create_user_schema, graphiql=True))(request)



