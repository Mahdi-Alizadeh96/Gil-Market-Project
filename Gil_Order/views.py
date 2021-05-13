from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Gil_Products.models import Product
from .forms import UserNewOrderForm
from .models import Order


@login_required
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        productId = new_order_form.cleaned_data.get('productId')
        product = Product.objects.get_by_id(product_id=productId)

        order.orderdetail_set.create(product_id=product.id, price=product.get_sale(), count=1)
        # todo: redirect user to user panel

    return redirect("/")
