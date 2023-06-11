from django.contrib import admin

from .models import Order

# Register your models here.


class order_admin(admin.ModelAdmin):
    list_filter = ("email", "product","vendor","category")
    list_display = ("FullName",'PhoneNumber','vendorName','vendorPhone','productName','categoryName','id','created'
                  )
    search_fields = ['email']

    def vendorName(self, obj):
        return obj.vendor.name
    
    def vendorPhone(self, obj):
        return obj.vendor.vendor_phoneNumber
    
    def categoryName(self, obj):
        return obj.category.Category_name
    
    def productName(self, obj):
        return obj.product.name
    
    
    def FullName(self, obj):
        fullName = obj.first_name + " " + obj.last_name
        return fullName
    

admin.site.register(Order, order_admin)