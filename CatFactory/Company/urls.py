from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Company.views import CompanyObjectsViewSet

router = DefaultRouter()
router.register(r'all', CompanyObjectsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
