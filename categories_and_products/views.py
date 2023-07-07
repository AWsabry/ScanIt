from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from graphene_django.views import GraphQLView
from .schema import all_Products_Query, get_all_vendors_schema,get_all_categories_schema,get_all_products_schema,get_vendor_by_id_schema,get_product_by_id_schema, get_products_by_category_slug_schema,get_all_subCategories_schema,get_subcategories_by_category_slug_schema


from categories_and_products.models import (
    Category,
    Product,
    SubCategory,
    Vendor,
    Gallery
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


def index(request):
    return render(request,"index.html")