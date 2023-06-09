import graphene
from graphene import InputObjectType, Mutation, String
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import Vendor,Category,Product

# Defining Models

# Vendors
class VendorType(DjangoObjectType):
    class Meta:
        model = Vendor
        fields = "__all__"

# Categories
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"

# Products
class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"


# Getting Vendors

# Getting all vendors
class all_Vendors_Query(graphene.ObjectType):
    all_vendors = graphene.List(VendorType)

    def resolve_all_vendors(self, info):
        return Vendor.objects.all()
    
# Getting Vendor By id
class Vendor_by_id_Query(graphene.ObjectType):
    get_vendor = graphene.Field(VendorType, id = graphene.String(required=True))
    
    def resolve_get_vendor(root, info, id):
        return Vendor.objects.get(id=id)
# End Getting Vendors


# Getting Categories

# Getting all categories
class all_Categories_Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)

    def resolve_all_categories(self, info):
        return Category.objects.all()
# End Getting Categories


# Getting Products

# Getting all products
class all_Products_Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    def resolve_all_products(self, info):
        return Product.objects.all()
    
# Getting Product By id
class Product_by_id_Query(graphene.ObjectType):
    get_product = graphene.Field(ProductType, id = graphene.String(required=True))
    
    def resolve_get_product(root, info, id):
        return Product.objects.get(id=id)
# End Getting Products


get_all_vendors_schema = graphene.Schema(query=all_Vendors_Query,)
get_vendor_by_id_schema = graphene.Schema(query=Vendor_by_id_Query,)

get_all_categories_schema = graphene.Schema(query=all_Categories_Query)

get_all_products_schema = graphene.Schema(query=all_Products_Query,)
get_product_by_id_schema = graphene.Schema(query=Product_by_id_Query,)
