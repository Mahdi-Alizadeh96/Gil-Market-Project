from django.http import Http404
from django.shortcuts import render
from .models import ProductBrand


def product_brand(request, *args, **kwargs):
    brand_name = kwargs['brand_name']
    brand = ProductBrand.objects.get_by_name(brand_name)

    if brand is None:
        raise Http404('صفحه مورد نظر یافت نشد')

    context = {
        'brand': brand,
    }
    return render(request, 'brand/brand.html', context)
