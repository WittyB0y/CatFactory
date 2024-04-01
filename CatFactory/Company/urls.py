from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Company.views import CompanyObjectsViewSet, GenerateQRCodeAndSendEmail

router = DefaultRouter()
router.register(r'all', CompanyObjectsViewSet, basename='company')
router.register(r'get_qr_code', GenerateQRCodeAndSendEmail, basename='qr_code')

urlpatterns = [
    path('', include(router.urls)),
]
