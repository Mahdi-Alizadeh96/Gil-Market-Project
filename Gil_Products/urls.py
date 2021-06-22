from django.urls import path
from .views import product_list, product_detail, ProductListByCategory, ProductCategoryBrand, SearchProducts, \
    DiscountView

urlpatterns = [
    path('products', product_list),
    path('products/<category_name>', ProductListByCategory.as_view()),
    path('products/<productId>/<name>', product_detail),
    path('result/<brand_name>/<category_name>', ProductCategoryBrand.as_view()),
    path('result/search', SearchProducts.as_view()),
    path('result/discount', DiscountView.as_view()),
]
