from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    search_fields = ('id', 'name', 'order')
    list_filter = ('id', 'name', 'order')


@admin.register(ProductSubcategory)
class ProductSubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'order')
    search_fields = ('id', 'category', 'name', 'order')
    list_filter = ('id', 'category', 'name', 'order')


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'name', 'specification', 'order')
    search_fields = ('id', 'subcategory', 'name', 'specification', 'order')
    list_filter = ('id', 'subcategory', 'name', 'specification', 'order')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_type', 'code', 'new_code', 'size', 'unit', 'package_qty', 'order')
    search_fields = ('id', 'product_type', 'code', 'new_code', 'size', 'unit', 'package_qty', 'order')
    list_filter = ('id', 'product_type', 'code', 'new_code', 'size', 'unit', 'package_qty', 'order')


@admin.register(ProductUnit)
class ProductUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit', 'package')
    search_fields = ('id', 'unit', 'package')
    list_filter = ('id', 'unit', 'package')


@admin.register(PriceCurrency)
class PriceCurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'decimal_number')
    search_fields = ('id', 'name', 'decimal_number')
    list_filter = ('id', 'name', 'decimal_number')


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'currency')
    search_fields = ('product', 'price', 'currency')
    list_filter = ('product', 'price', 'currency')
