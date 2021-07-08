from django.shortcuts import get_object_or_404, render
from .models import ProductBrand


def product_brand(request, *args, **kwargs):
    brand_name = kwargs.get('brand_name')
    brand = get_object_or_404(ProductBrand, name=brand_name)
  
    context = {
        'brand': brand,
    }
    return render(request, 'brand/brand.html', context)
