from Register_Login.models import Profile, Team_Member,ContactUs
from django.contrib import admin

# Register your models here.




class Register(admin.ModelAdmin):
    list_filter = ("email","first_name", "last_name", "last_modified")
    list_display = ("email","first_name", 'last_name','last_modified','PhoneNumber','is_active','id','otp'
                  )
    search_fields = ['email']



class Team_Admin(admin.ModelAdmin):
    model = Team_Member
    list_display = ('first_name','last_name','email','PhoneNumber')


class AccessTokenAdmin(admin.ModelAdmin):
    model = Profile
    fieldsets = (
        (None, {"fields": (
                'user', 'token', 'expires', 'created'
            )}),
    )
    readonly_fields = ('token','created')
    list_display = ('user', 'token', 'created')






admin.site.register(Profile, Register)
admin.site.register(ContactUs,)

admin.site.register(Team_Member, Team_Admin)


