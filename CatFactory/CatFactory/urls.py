from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('Company.urls')),
    path('product/', include('Product.urls')),
]
