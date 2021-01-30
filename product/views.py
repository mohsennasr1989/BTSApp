from .models import Product
from rest_framework import viewsets


class AllProductsList(viewsets.ModelViewSet):
    model = Product
    queryset = Product.objects.all()
    paginate_by = 5
    context_object_name = 'products'
    template_name = 'product/index.html'
