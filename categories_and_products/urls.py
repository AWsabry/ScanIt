from django.urls import path
from .views import getVendors,getProducts, getCategories,getVendorsById,getProductById

app_name = 'categories_and_products'


urlpatterns = [
    
    path('getVendors/',view=getVendors, name= "getVendors"),
    path('getVendorsById/',view=getVendorsById, name= "getVendorsById"),

    path('getCategories/',view=getCategories, name= "getCategories"),

    path('getProducts/',view=getProducts, name= "getProducts"),
    path('getProductById/',view=getProductById, name= "getProductById"),


]
