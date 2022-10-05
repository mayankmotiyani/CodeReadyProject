from django.contrib import admin
from .models import (
    Product,
    ProductCategory,
    ProductSubCategory
)

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    # list_display = "__all__"
    exclude = ["product_slug"]

    ordering = ['id']

admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    list_display = ['id','category','created','updated']

    ordering = ['created']

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductSubCategoryAdmin(admin.ModelAdmin):
    model = ProductSubCategory
    list_display = ['id','category','subcategory','created','updated']

    ordering = ['created']

admin.site.register(ProductSubCategory, ProductSubCategoryAdmin)