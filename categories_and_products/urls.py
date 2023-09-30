from django.urls import path
from .views import getVendors,getProducts, getCategories,getVendorsById,getProductById,index,get_products_by_category_slug,getSubCategories,get_subcategories_by_category_slug,get_New_Products,get_bestOffer_products,get_mostSold_products
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
    path('get_New_Products/',view=get_New_Products.as_view(), name= "get_New_Products"),
    path('get_mostSold_products/',view=get_mostSold_products.as_view(), name= "get_mostSold_products"),
    path('get_bestOffer_products/',view=get_bestOffer_products.as_view(), name= "get_bestOffer_products"),

    path('get_subCategory_by_category_slug/',view=get_subcategories_by_category_slug, name= "get_subCategory_by_category_slug"),
    path('get_searched_products/<str:searched>', views.get_searched_products.as_view(), name='get_searched_products'),
    
    
    path('video/',views.get_video.as_view(), name= "video"),
    path('gallery/<int:id>',views.get_gallery.as_view(), name= "gallery"),
    path('getProductById/',view=getProductById, name= "getProductById"),
]
