from rest_framework import viewsets, permissions
from Product.models import Product
from Product.serializer import ProductObjectsSerializer


class ProductObjectsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductObjectsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ("get", "post",)
