from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,Group
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.timezone import timedelta
from django.utils import timezone
from scanit import settings

from Register_Login.utils import AccessTokenGenerator
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

time_choices = (
    ('11:00 AM','11:00 AM'),
    ('01:00 PM', '01:00 PM'),
    ('03:00 PM','03:00 PM'),
)


class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        """
        To make email login case sensetive.
        """
        
        return self.get(email__iexact=username)

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        
        if not email:
            raise ValueError('Email does not included!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        return self.create_user(email=email, password=password, **extra_fields)

class Profile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    city = models.CharField(max_length=10, null=True,blank = True)
    PhoneNumber =  models.CharField(max_length=20, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_vendor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    email = models.EmailField(max_length=500, blank=True)
    def __str__(self):
        return self.email





class AccessToken(models.Model):
    token = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(to= Profile, on_delete=models.CASCADE, related_name='token')
    expires = models.DateTimeField()
    created = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return self.token
    
    class Meta:
        ordering = ('-created',)

@receiver(pre_save, sender=AccessToken)
def token_save(sender, instance, **kwargs):
    instance.token = AccessTokenGenerator().make_token(instance.user)
    instance.expires = timezone.now() + timedelta(seconds=settings.AUTH_EMAIL_ACTIVATE_EXPIRE)
    

class Team_Member(models.Model):
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(max_length=50, null=True,blank = True)
    last_name = models.CharField(max_length=50, null=True,blank = True)
    is_active = models.BooleanField(default=True,blank = True)
    profile_pic = models.ImageField(
        upload_to="Team", blank=True, )
    job_title = models.CharField(max_length=100, null=True,blank = True)
    Facebook_Link = models.CharField(max_length=500, null=True,blank = True)
    LinkedInLink = models.CharField(max_length=500, null=True,blank = True)
    nu_id = models.CharField(max_length=60, null=True,blank = True)
    school = models.CharField(max_length=60, null=True,blank = True)
    PhoneNumber =  models.CharField(max_length=20, null=True,blank = True)
    last_modified = models.DateTimeField(auto_now=True,blank = True)
    # ProfilePic = models.ImageField(upload_to="profile/", null=True)

    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = "Team members"
