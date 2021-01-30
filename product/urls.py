from django.urls import path

from .views import AllProductsList

app_name = 'product'

urlpatterns = [
    path('', AllProductsList.as_view(), name='products'),
]
