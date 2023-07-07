from django.contrib import admin
from categories_and_products.models import Location, Poster,Category, Product, Vendor, SubCategory

# Register your models here.

class Categories_Admin(admin.ModelAdmin):
    # prepopulated_fields = {'category_slug': ('Category_name',), }
    list_filter = ("Category_name", "created",)
    list_display = ('Category_name', "created","active","id","category_slug")
    search_fields = ['Category_name']
    list_editable=['active']

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["image"].help_text = " * width: 700, height: 800px are recommended"
        return form


class SubCategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'category_slug': ('Category_name',), }
    list_filter = ("SubCategory_name", "created",)
    list_display = ('SubCategory_name', "created","active","id",)
    search_fields = ['SubCategory_name']
    list_editable=['active']

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["image"].help_text = " * width: 700, height: 800px are recommended"
        return form
    


class Vendor_Admin(admin.ModelAdmin):
    # prepopulated_fields = {'vendor_slug': ('name',), }
    list_display = ("name","created","id","vendor_phoneNumber", "active",)
    search_fields = ['name']
    list_editable=['active',]

class ProductAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'product_slug': ('name','vendor',), }
    list_filter = ("name", "category", "vendor", "created")
    list_display = ('name', "start_from","reach_to", 'vendor', "category",
                     "id", "created","Best_Offer", "Most_Popular","New_Products","active",)
    # inlines = [ProductsFile,]
    list_display_links = [
        'name',
        'category',
    ]
    search_fields = ['name']
    list_editable=['active']
    


class Poster_Admin(admin.ModelAdmin):
    list_display = ("name","active")



admin.site.register(Category, Categories_Admin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Vendor,Vendor_Admin)
admin.site.register(Poster,Poster_Admin)
admin.site.register(Location)
admin.site.register(SubCategory, SubCategoryAdmin)


# admin.site.register(PromoCode, PromoCodeAdmin)
