from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import all_Products_Query, get_all_vendors_schema,get_all_categories_schema,get_all_products_schema,get_vendor_by_id_schema,get_product_by_id_schema, get_products_by_category_slug_schema,get_all_subCategories_schema,get_subcategories_by_category_slug_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from categories_and_products.models import Product
from orders.models import Order
from django.http import JsonResponse
from categories_and_products.serializers import ProductsSerializer,VideoSerializer,GallerySerializer
from categories_and_products.models import (
    Category,
    Product,
    SubCategory,
    Vendor,
    Gallery,
    Video
)




@csrf_exempt
def getVendors(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_all_vendors_schema, graphiql=True))(request)


@csrf_exempt
def getVendorsById(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_vendor_by_id_schema, graphiql=True))(request)


@csrf_exempt
def getCategories(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_all_categories_schema, graphiql=True))(request)

@csrf_exempt
def getSubCategories(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_all_subCategories_schema, graphiql=True))(request)

@csrf_exempt
def get_subcategories_by_category_slug(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_subcategories_by_category_slug_schema, graphiql=True))(request)



@csrf_exempt
def get_products_by_category_slug(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_products_by_category_slug_schema, graphiql=True))(request)

@csrf_exempt
def getProducts(request):
    
    return csrf_exempt(GraphQLView.as_view(schema=get_all_products_schema, graphiql=True))(request)

@csrf_exempt
def getProductById(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_product_by_id_schema, graphiql=True))(request)


# Getting Searched Products
class get_searched_products(APIView):
    def get(self,request,searched):
        if searched:
            englishName = Product.objects.filter(active = True,name__icontains = searched,)
            englishSerializer = ProductsSerializer(englishName,many = True,)
            if englishName :
               return JsonResponse({"Names": englishSerializer.data}, safe=False)
            else:
                return JsonResponse("No Data Found", safe=False)
        else:
            return JsonResponse('No Values Found', safe=False)

# Getting Video
class get_video(APIView):
    def get(self, request):
        all = Video.objects.all()
        serializer = VideoSerializer(all, many = True)
        return JsonResponse({"Video": serializer.data}, safe=False)
    


# Getting Images
class get_gallery(APIView):
    def get(self, request,id):
        all = Gallery.objects.filter(product__id=id)
        serializer = GallerySerializer(all, many = True)
        return JsonResponse({"Images": serializer.data}, safe=False)
    
    
      
def index(request):
    return render(request,"index.html")