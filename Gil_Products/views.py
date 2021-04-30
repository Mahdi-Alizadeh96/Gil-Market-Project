from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.http import Http404
from Gil_Products_Category.models import ProductCategory


class ProductList(ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductListByCategory(ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد!")
        return Product.objects.get_product_by_category(category_name)


def product_detail(request, *args, **kwargs):
    product_id = kwargs['productId']

    product = Product.objects.get_by_id(product_id)

    if product is None:
        raise Http404('محصول مورد نظر یافت نشد!')

    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)
