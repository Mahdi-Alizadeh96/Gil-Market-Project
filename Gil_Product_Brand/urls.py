from django.urls import path

from .views import product_brand

app_name = "brand"
urlpatterns = [
    path('brands/<brand_name>', product_brand, name='p_brand')
]
