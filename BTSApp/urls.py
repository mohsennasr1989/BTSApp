"""BTSApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product.api import views as product_view
from translate.api import views as translate_view
from user.api import views as user_view

router = routers.SimpleRouter()
router.register('product-category', product_view.ProductCategoryViewSet, basename='product-category')
router.register('product-subcategory', product_view.ProductSubcategoryViewSet, basename='product-subcategory')
router.register('product-type', product_view.ProductTypeViewSet, basename='product-type')
router.register('product-unit', product_view.ProductUnitViewSet, basename='product-unit')
router.register('product-price', product_view.ProductPriceViewSet, basename='product-price')
router.register('product', product_view.ProductViewSet, basename='product')
router.register('price-currency', product_view.PriceCurrencyViewSet, basename='price-currency')
router.register('translate', translate_view.DictionaryViewSet, basename='translate')
router.register('user', user_view.CustomUserViewSet, basename='user')

app_name = 'bts_app'
urlpatterns = [
                  path('', include(router.urls)),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
