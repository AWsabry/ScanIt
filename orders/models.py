from django.db import models
from django.conf import settings
from Register_Login.models import Profile
from categories_and_products.models import Vendor, Product,Category
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

    

class Order(models.Model):
    email = models.EmailField(verbose_name='Email address',)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True,blank = True)
    address =  models.CharField(max_length=500, blank=True, null= True)
    PhoneNumber =  models.CharField(max_length=20, null=True,)
    created = models.DateTimeField(auto_now=True, editable=False)
    vendor = models.ForeignKey(to= Vendor, on_delete=models.CASCADE, related_name='vendor',verbose_name='vendor')
    category = models.ForeignKey(to= Category, on_delete=models.CASCADE, related_name='category',verbose_name='category')
    product = models.ForeignKey(to= Product, on_delete=models.CASCADE, related_name='product',verbose_name='product')

    
    def __str__(self):
        return self.email
    
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
    percentage = models.FloatField(default=0.0, validators=[
                                   MinValueValidator(0.0), MaxValueValidator(1.0)], blank=True, null=True,)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    vendor = models.ForeignKey(to= Vendor, on_delete=models.CASCADE, related_name='promo_vendor',verbose_name='promo_vendor')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,related_name='promo_user',verbose_name='promo_user')

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        self.percentage = round(self.percentage, 2)
        super(PromoCode, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "PromoCodes"