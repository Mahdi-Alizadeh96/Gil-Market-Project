from django.urls import path
from .views import product_list, product_detail, ProductListByCategory, ProductCategoryBrand, SearchProducts, \
    DiscountView

app_name = 'product'
urlpatterns = [
    path('products', product_list, name='product'),
    path('products/<category_name>', ProductListByCategory.as_view(), name='p_category'),
    path('products/<productId>/<name>', product_detail, name='product_detail'),
    path('result/<brand_name>/<category_name>', ProductCategoryBrand.as_view(), name='p_category_brand'),
    path('result/search', SearchProducts.as_view(), name='search'),
    path('result/discount', DiscountView.as_view(), name='discount'),
]
