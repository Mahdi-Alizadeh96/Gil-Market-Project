from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView

from Gil_Order.forms import UserNewOrderForm
from Gil_Product_Brand.models import ProductBrand
from .models import Product
from django.http import Http404
from Gil_Products_Category.models import ProductCategory
from django.db.models import Count


def product_list(request):
    context = {}
    return render(request, 'products/product_list.html', context)


class ProductListByCategory(ListView):
    template_name = 'products/p_category_list.html'
    paginate_by = 12

    def get_queryset(self):
        global category
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد!")
        if self.request.GET.get('status'):
            status_filter = self.request.GET.get('status')
            if status_filter == "high":
                return Product.objects.get_product_by_category(category_name).order_by('-price')
            elif status_filter == "low":
                return Product.objects.get_product_by_category(category_name).order_by('price')
            elif status_filter == "new":
                return Product.objects.get_product_by_category(category_name).order_by('-id')
            elif status_filter == "hit":
                return Product.objects.get_product_by_category(category_name).annotate(count=Count('hits')).order_by('-count')
        else:
            return Product.objects.get_product_by_category(category_name)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class ProductCategoryBrand(ListView):
    template_name = 'products/p_category_brand.html'
    paginate_by = 12

    def get_queryset(self):
        global brand
        global category
        brand_name = self.kwargs['brand_name']
        category_name = self.kwargs['category_name']
        brand = ProductBrand.objects.get_by_name(brand_name)
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if brand and category is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        if self.request.GET.get('status'):
            status_filter = self.request.GET.get('status')
            if status_filter == "high":
                return Product.objects.get_product_by_category_brand(brand_name, category_name).order_by('-price')
            elif status_filter == "low":
                return Product.objects.get_product_by_category_brand(brand_name, category_name).order_by('price')
            elif status_filter == "new":
                return Product.objects.get_product_by_category_brand(brand_name, category_name).order_by('-id')
            elif status_filter == "hit":
                return Product.objects.get_product_by_category_brand(brand_name, category_name).annotate(count=Count('hits')).order_by('-count')
        else:
            return Product.objects.get_product_by_category_brand(brand_name, category_name)
    
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = brand
        context['category'] = category
        return context


def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    new_order_form = UserNewOrderForm(request.POST or None, initial={'productId': selected_product_id})

    product = Product.objects.get_by_id(selected_product_id)
    if product is None:
        raise Http404('محصول مورد نظر یافت نشد!')

    ip_address = request.user.ip_address
    if ip_address not in product.hits.all():
        product.hits.add(ip_address)

    context = {
        'product': product,
        'new_order_form': new_order_form
    }
    return render(request, 'products/product_detail.html', context)


class SearchProducts(ListView):
    template_name = 'products/search.html'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query is not None:
            return Product.objects.search(query)
        else:    
            raise Http404('محصول مورد نظر یافت نشد!')
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context


class DiscountView(ListView):
    template_name = 'products/discount.html'
    paginate_by = 12

    def get_queryset(self):
        if self.request.GET.get('status'):
            status_filter = self.request.GET.get('status')
            if status_filter == "high":
                return Product.objects.filter(~Q(discount=0), active=True).order_by('-price')
            elif status_filter == "low":
                return Product.objects.filter(~Q(discount=0), active=True).order_by('price')
            elif status_filter == "new":
                return Product.objects.filter(~Q(discount=0), active=True).order_by('-id')
            elif status_filter == "hit":
                return Product.objects.filter(~Q(discount=0), active=True).annotate(count=Count('hits')).order_by('-count')
        else:
            return Product.objects.filter(~Q(discount=0), active=True)