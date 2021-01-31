from rest_framework import viewsets
from .serializers import ProductCategorySerializer, ProductSubcategorySerializer, ProductTypeSerializer, \
    ProductSerializer, ProductUnitSerializer, ProductPriceSerializer, PriceCurrencySerializer
from .models import ProductCategory, ProductSubcategory, ProductType, Product, ProductUnit, ProductPrice, PriceCurrency


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductSubcategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductSubcategory.objects.all()
    serializer_class = ProductSubcategorySerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUnitViewSet(viewsets.ModelViewSet):
    queryset = ProductUnit.objects.all()
    serializer_class = ProductUnitSerializer


class ProductPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer


class PriceCurrencyViewSet(viewsets.ModelViewSet):
    queryset = PriceCurrency.objects.all()
    serializer_class = PriceCurrencySerializer
