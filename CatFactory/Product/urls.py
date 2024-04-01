from django.urls import include, path
from rest_framework.routers import DefaultRouter
from Product.views import ProductObjectsViewSet

router = DefaultRouter()
router.register(r'all', ProductObjectsViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
