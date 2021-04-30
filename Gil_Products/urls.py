from django.urls import path
from .views import ProductList, product_detail, ProductListByCategory

urlpatterns = [
    path('products', ProductList.as_view()),
    path('products/<category_name>', ProductListByCategory.as_view()),
    path('products/<productId>/<name>', product_detail),
]
