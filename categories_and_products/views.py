from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from graphene_django.views import GraphQLView
from .schema import get_all_vendors_schema,get_all_categories_schema,get_all_products_schema,get_vendor_by_id_schema,get_product_by_id_schema


from categories_and_products.models import (
    Category,
    Product,
    Vendor,
    Poster
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
def getProducts(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_all_products_schema, graphiql=True))(request)

@csrf_exempt
def getProductById(request):
    return csrf_exempt(GraphQLView.as_view(schema=get_product_by_id_schema, graphiql=True))(request)


def index(request):
    return render(request,"index.html")