from django.urls import path
from .views import getVendors,getProducts, getCategories,getVendorsById,getProductById,index,get_products_by_category_slug,getSubCategories,get_subcategories_by_category_slug
from . import views
app_name = 'categories_and_products'


urlpatterns = [
    
    path('getVendors/',view=getVendors, name= "getVendors"),
    path('getVendorsById/',view=getVendorsById, name= "getVendorsById"),
    path('',view=index, name= "index"),
    path('getCategories/',view=getCategories, name= "getCategories"),
    path('getSubCategories/',view=getSubCategories, name= "getSubCategories"),
    path('get_products_by_category_slug/',view=get_products_by_category_slug, name= "get_products_by_category_slug"),
    path('getProducts/',view=getProducts, name= "getProducts"),
    path('get_subCategory_by_category_slug/',view=get_subcategories_by_category_slug, name= "get_subCategory_by_category_slug"),
    path('get_searched_products/<str:searched>', views.get_searched_products.as_view(), name='get_searched_products'),
    
    
    path('video/',views.get_video.as_view(), name= "video"),
    path('gallery/<int:id>',views.get_gallery.as_view(), name= "gallery"),
    path('getProductById/',view=getProductById, name= "getProductById"),
]
