from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductCategorySerializer, ProductSubcategorySerializer, ProductTypeSerializer, \
    ProductSerializer, ProductUnitSerializer, ProductPriceSerializer, PriceCurrencySerializer
from product.models import ProductCategory, ProductSubcategory, ProductType, Product, ProductUnit, ProductPrice, PriceCurrency


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def list(self, request, **kwargs):
        serializer = ProductCategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        category = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductCategorySerializer(category)
        return Response(serializer.data)


class ProductSubcategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductSubcategory.objects.all()
    serializer_class = ProductSubcategorySerializer

    def list(self, request, **kwargs):
        serializer = ProductSubcategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        subcategory = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductSubcategorySerializer(subcategory)
        return Response(serializer.data)


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    def list(self, request, **kwargs):
        serializer = ProductTypeSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        product_type = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductTypeSerializer(product_type)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, **kwargs):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductUnitViewSet(viewsets.ModelViewSet):
    queryset = ProductUnit.objects.all()
    serializer_class = ProductUnitSerializer

    def list(self, request, **kwargs):
        serializer = ProductUnitSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        product_unit = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductUnitSerializer(product_unit)
        return Response(serializer.data)


class ProductPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer

    def list(self, request, **kwargs):
        serializer = ProductPriceSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        product_price = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductPriceSerializer(product_price)
        return Response(serializer.data)


class PriceCurrencyViewSet(viewsets.ModelViewSet):
    queryset = PriceCurrency.objects.all()
    serializer_class = PriceCurrencySerializer

    def list(self, request, **kwargs):
        serializer = PriceCurrencySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        product_currency = get_object_or_404(self.queryset, pk=pk)
        serializer = PriceCurrencySerializer(product_currency)
        return Response(serializer.data)
