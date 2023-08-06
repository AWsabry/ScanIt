from django.db import models
from django.conf import settings
from Register_Login.models import Profile
from categories_and_products.models import Vendor, Product,Category
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

import string
import random

# Create your models here.
N=11
    

class Order(models.Model):
    email = models.EmailField(verbose_name='Email address',)
    PhoneNumber =  models.CharField(max_length=20, null=True,)
    created = models.DateTimeField(auto_now=True, editable=False)
    product = models.ForeignKey(to= Product, on_delete=models.CASCADE, related_name='product',verbose_name='product')
    code =  models.CharField(max_length=36,editable=False,unique=True)
    vendor = models.ForeignKey(to= Vendor, on_delete=models.CASCADE, related_name='vendor',verbose_name='vendor',null=True,blank=True)

    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
        substring = str(self.PhoneNumber[3:5])
        self.code = res + substring
        super(Order, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)



# class CartItems(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE,null=True)
#     order = models.ForeignKey(
#         Order, on_delete=models.CASCADE, null = True, blank=True)
#     ordered = models.BooleanField(default=False)
#     paid = models.BooleanField(default=False)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     totalOrderItemPrice = models.PositiveIntegerField(default=0)
#     vendor = models.ForeignKey(
#         Vendor, on_delete=models.CASCADE, blank=True,null= True)
    
    
        
#     def __str__(self):
#         return str(self.user.email) + " " + str(self.product)


class PromoCode(models.Model):
    code = models.CharField(
        max_length=10, unique=True, blank=True, null=True)
    # percentage = models.FloatField(default=0.0, validators=[
    #                               MinValueValidator(0.0), MaxValueValidator(1.0)], blank=True, null=True,)
    # created = models.DateTimeField(auto_now_add=True)
    # active = models.BooleanField(default=False)
    # vendor = models.ForeignKey(to= Vendor, on_delete=models.CASCADE, related_name='promo_vendor',verbose_name='promo_vendor')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE,related_name='promo_user',verbose_name='promo_user')

    def __str__(self):
        return str(self.code)

    def save(self, *args, **kwargs):
        self.percentage = round(self.percentage, 2)
        super(PromoCode, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "PromoCodes"