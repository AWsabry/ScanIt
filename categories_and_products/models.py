
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.db import models
from django.utils.text import slugify

from scanit import settings

# Create your models here.
class Location(models.Model):
    country = models.CharField(max_length=250, blank=True,null = True,)
    city = models.CharField(max_length=250, blank=True,null = True,)
    address = models.CharField(max_length=50, null=True,blank=True)
    Longitude = models.FloatField(default=0,null=True, blank= True)
    Latitude = models.FloatField(default=0,null=True, blank= True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.city)

    
    class Meta:
        verbose_name_plural = "Locations"


def upload_vendor_images(instance, filename):
    return 'Vendors/%s/Profile/%s' % (instance.name, filename)


class Vendor(models.Model):
    name = models.CharField(max_length=250, blank=True, unique=True,null = True)
    vendor_slug = models.SlugField(unique=True, db_index=True,editable=False)
    vendor_phoneNumber = models.CharField(max_length=250, blank=True, unique=True,null = True)
    number_of_branches = models.IntegerField(default= 1, blank = True, null = True)
    vendor_type = models.CharField(max_length=250, blank=True,null = True)
    logo_image = models.ImageField(
        upload_to=upload_vendor_images, blank=True, )
    background_image = models.ImageField(
        upload_to=upload_vendor_images, blank=True, )
    Longitude = models.FloatField(default=0,null=True, blank= True)
    Latitude = models.FloatField(default=0,null=True, blank= True)
    created = models.DateTimeField(auto_now_add=True)
    locations = models.ManyToManyField(Location,blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url_restaurant(self):
        return reverse('categories_and_products:menu', args=[self.restaurant_slug])
    
    def save(self, *args, **kwargs):
        self.vendor_slug = slugify(self.name)
        super(Vendor, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Vendors"




class Category(models.Model):
    Category_name = models.CharField(max_length=250,unique = True,)
    category_slug = models.SlugField(unique=True, db_index=True,blank=True,null = True,editable=False)
    image = models.ImageField(
        upload_to="Categories", blank=True,null = True )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.Category_name)
        
        
    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.Category_name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url_category(self):
        return reverse('categories_and_products:category_details', args=[self.Restaurant.restaurant_slug] + [self.categoryslug])

    class Meta:
        verbose_name_plural = "Categories"

def get_upload_to(instance, filename):
    return 'Vendors/%s/%s' %(instance.vendor, filename)

class SubCategory(models.Model):
    SubCategory_name = models.CharField(max_length=250,unique = True,)
    subCategory_slug = models.SlugField(unique=True, db_index=True,blank=True,null = True,editable=False)
    image = models.ImageField(
        upload_to="Categories", blank=True,null = True )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True,null= True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.SubCategory_name)
    
    def save(self, *args, **kwargs):
        self.subCategory_slug = slugify(self.SubCategory_name)
        super(SubCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Sub-Categories"


class Product(models.Model):
    name = models.CharField(max_length=250, blank=True)
    product_slug = models.SlugField(unique=True, db_index=True,editable=False)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, blank=True,null= True)
    description = models.TextField(blank=True)
    start_from = models.FloatField(default=0)
    reach_to = models.FloatField(default=0)
    image = models.ImageField(
        upload_to=get_upload_to, blank=True, )
    file =  models.FileField(upload_to= get_upload_to)
    active = models.BooleanField(default=True)
    SubCategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE, blank=True,null= True)
    Most_Popular = models.BooleanField(default=False)
    New_Products = models.BooleanField(default=False)
    Best_Offer = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories_and_products:product_details", args=[self.vendors.vendors_slug] + [self.product_slug])
    
    def get_absolute_searched_url(self):
        return reverse("categories_and_products:searched_Page_Restaurants_Products", args=[self.vendors.vendors_slug])
    
    def save(self, *args, **kwargs):
        self.product_slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Poster(models.Model):
    name = models.CharField(max_length=250, blank=True, unique=True)
    background_image = models.ImageField(
        upload_to="Mobile_Poster", blank=True,)
    active = models.BooleanField(default=True)


