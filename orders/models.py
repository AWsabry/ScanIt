from django.db import models

from categories_and_products.models import Vendor, Product,Category

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