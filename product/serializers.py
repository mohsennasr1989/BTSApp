from rest_framework import serializers

from .models import *


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'order']


class ProductSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubcategory
        fields = ['id', 'category', 'name', 'order']


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'subcategory', 'name', 'specification', 'technical_detail', 'site_link', 'image', 'order']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_type', 'code', 'new_code', 'size', 'unit', 'package_qty', 'order']


class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ['id', 'tag', 'product', 'price', 'currency']


class ProductUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ['id', 'name', 'unit', 'package']


class PriceCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCurrency
        fields = ['id', 'name', 'decimal_number']
