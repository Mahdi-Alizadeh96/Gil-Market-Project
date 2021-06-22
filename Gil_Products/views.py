from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
from Gil_Comment.forms import CommentForm
from Gil_Comment.models import Comments
from Gil_Order.forms import UserNewOrderForm
from Gil_Product_Brand.models import ProductBrand
from .models import Product
from django.http import Http404
from Gil_Products_Category.models import ProductCategory


def product_list(request, *args, **kwargs):
    context = {}
    return render(request, 'products/product_list.html', context)


class ProductListByCategory(ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد!")
        return Product.objects.get_product_by_category(category_name)


class ProductCategoryBrand(ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        brand_name = self.kwargs['brand_name']
        category_name = self.kwargs['category_name']
        brand = ProductBrand.objects.get_by_name(brand_name)
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if brand and category is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Product.objects.get_product_by_category_brand(brand_name, category_name)


def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    new_order_form = UserNewOrderForm(request.POST or None, initial={'productId': selected_product_id})

    product = Product.objects.get_by_id(selected_product_id)

    if product is None:
        raise Http404('محصول مورد نظر یافت نشد!')

    comments = product.comments.filter(active=True)

    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        name = comment_form.cleaned_data.get('name')
        message = comment_form.cleaned_data.get('message')
        Comments.objects.create(product=product, name=name, message=message)
        return redirect(f'/products/{product.id}/{product.name_fa}')

    context = {
        'product': product,
        'comments': comments,
        'comment_form': comment_form,
        'new_order_form': new_order_form
    }
    return render(request, 'products/product_detail.html', context)


class SearchProducts(ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return None


class DiscountView(ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        return Product.objects.filter(~Q(discount=0), active=True)
