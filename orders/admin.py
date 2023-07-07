from django.contrib import admin

from .models import Order, PromoCode

# Register your models here.


class order_admin(admin.ModelAdmin):
    list_filter = ("email", "product","vendor","category")
    list_display = ("full_name",'PhoneNumber','vendor_name','vendor_Phone','productName','categoryName','id','created','code'
                  )
    search_fields = ['email']

    def vendor_name(self, obj):
        return obj.vendor.name
    
    def vendor_Phone(self, obj):
        return obj.vendor.vendor_phoneNumber
    
    def categoryName(self, obj):
        return obj.category.Category_name
    
    def productName(self, obj):
        return obj.product.name
    
    
    def full_name(self, obj):
        fullName = obj.first_name + " " + obj.last_name
        return fullName


class PromoCodeAdmin(admin.ModelAdmin):
    list_filter = ("user","vendor",)
    list_display = ("username","code",'full_name','vendor_name','vendor_Phone','user_phone','created','active')
    search_fields = ['user__email','user__PhoneNumber','vendor__name']

    def vendor_name(self, obj):
        if not obj.vendor:
            return "Empty"
        return obj.vendor.name
    
    def user_phone(self, obj):
        if not obj.user:
            return "Empty"
        return obj.user.PhoneNumber

    def full_name(self, obj):
        fullName = obj.user.first_name + " " + obj.user.last_name
        if not fullName:
            return "Empty"
        return fullName
    

    def username(self, obj):
        if not obj.user:
            return "Empty"
        return obj.user.email
    
    def vendor_Phone(self, obj):
        if not obj.vendor:
            return "Empty"
        return obj.vendor.vendor_phoneNumber



admin.site.register(Order, order_admin)
admin.site.register(PromoCode, PromoCodeAdmin)