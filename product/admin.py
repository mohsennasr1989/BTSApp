from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats


# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdmin(ImportExportModelAdmin, ModelAdmin):
    model = ProductCategory
    list_display = ('id', 'name', 'order')
    search_fields = ('id', 'name', 'order')
    list_filter = ('id', 'name', 'order')
    export_order = ('id', 'name', 'order')

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]


@admin.register(ProductSubcategory)
class ProductSubcategoryAdmin(ImportExportModelAdmin, ModelAdmin):
    model = ProductSubcategory
    list_display = ('id', 'category', 'name', 'order')
    search_fields = ('id', 'category', 'name', 'order')
    list_filter = ('id', 'category', 'name', 'order')
    export_order = ('id', 'category', 'name', 'order')

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]


@admin.register(ProductType)
class ProductTypeAdmin(ImportExportModelAdmin, ModelAdmin):
    model = ProductType
    list_display = ('id', 'subcategory', 'name', 'specification', 'order')
    search_fields = ('id', 'subcategory', 'name', 'specification', 'order')
    list_filter = ('id', 'subcategory', 'name', 'specification', 'order')
    export_order = ('id', 'subcategory', 'name', 'specification', 'order')

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, ModelAdmin):
    model = ProductUnit
    list_display = ('id', 'product_type', 'code', 'new_code', 'size', 'unit', 'package_qty', 'order')
    search_fields = ('id', 'product_type', 'code', 'new_code', 'size', 'unit', 'package_qty', 'order')
    list_filter = ('id', 'product_type', 'code', 'new_code', 'size', 'unit', 'package_qty', 'order')
    export_order = ('id', 'product_type', 'code', 'new_code', 'size', 'unit', 'package_qty', 'order')

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]


@admin.register(ProductUnit)
class ProductUnitAdmin(ImportExportModelAdmin, ModelAdmin):
    model = ProductUnit
    list_display = ('id', 'name', 'unit', 'package')
    search_fields = ('id', 'name', 'unit', 'package')
    list_filter = ('id', 'name', 'unit', 'package')
    export_order = ('id', 'name', 'unit', 'package')

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]


@admin.register(PriceCurrency)
class PriceCurrencyAdmin(ImportExportModelAdmin, ModelAdmin):
    model = PriceCurrency
    list_display = ('id', 'name', 'decimal_number')
    search_fields = ('id', 'name', 'decimal_number')
    list_filter = ('id', 'name', 'decimal_number')
    export_order = ('id', 'name', 'decimal_number')

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]


@admin.register(ProductPrice)
class ProductPriceAdmin(ImportExportModelAdmin, ModelAdmin):
    model = ProductPrice
    list_display = ('product', 'price', 'currency')
    search_fields = ('product', 'price', 'currency')
    list_filter = ('product', 'price', 'currency')
    export_order = ('product', 'price', 'currency')

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]
