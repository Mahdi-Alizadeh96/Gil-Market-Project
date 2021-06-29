from django.urls import path
from .views import product_list, product_detail, ProductListByCategory, ProductCategoryBrand, SearchProducts, \
    DiscountView

app_name = 'product'
urlpatterns = [
    path('products', product_list, name='product'),
    path('products/<int:productId>/<slug:slug>', product_detail, name='product_detail'),
    path('products/<category_name>', ProductListByCategory.as_view(), name='p_category'),
    path('products/<category_name>/page/<int:page>', ProductListByCategory.as_view(), name='p_category'),
    path('result/<brand_name>/<category_name>', ProductCategoryBrand.as_view(), name='p_category_brand'),
    path('result/<brand_name>/<category_name>/page/<int:page>', ProductCategoryBrand.as_view(), name='p_category_brand'),
    path('result/search/', SearchProducts.as_view(), name='search'),
    path('result/search/page/<int:page>', SearchProducts.as_view(), name='search'),
    path('result/discount', DiscountView.as_view(), name='discount'),
    path('result/discount/page/<int:page>', DiscountView.as_view(), name='discount'),
]
