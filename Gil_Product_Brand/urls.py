from django.urls import path

from .views import product_brand

urlpatterns = [
    path('brands/<brand_name>', product_brand)
]
