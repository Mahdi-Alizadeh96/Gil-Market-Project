from django.contrib.auth.decorators import login_required
from django.http import Http404
from base_user_account.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm, EditUserForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Gil_Products.models import Product
from Gil_Order.models import Order
from .mixins import FieldsMixin, AdminAccessMixin


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        phone = login_form.cleaned_data.get('phone')
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error("phone", 'کاربری با این مشخصات یافت نشد')

    context = {
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        phone = register_form.cleaned_data.get('phone')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(
            first_name=first_name, last_name=last_name, phone=phone,
            email=email, address=None, password=password
        )
        return redirect('account:login')

    context = {
        'register_form': register_form
    }
    return render(request, 'account/register.html', context)


def log_out(request):
    logout(request)
    return redirect('account:login')


@login_required(login_url='account:login')
def user_panel(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'account/user_panel.html', context)


@login_required(login_url='account:login')
def edit_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    edit_user_form = EditUserForm(request.POST or None,
                                  initial={'first_name': user.first_name, 'last_name': user.last_name,
                                           'phone': user.phone, 'email': user.email, 'address': user.address}
                                  )
    if edit_user_form.is_valid():
        first_name = edit_user_form.cleaned_data.get('first_name')
        last_name = edit_user_form.cleaned_data.get('last_name')
        phone = edit_user_form.cleaned_data.get('phone')
        email = edit_user_form.cleaned_data.get('email')
        address = edit_user_form.cleaned_data.get('address')

        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.email = email
        user.address = address
        user.save()

    context = {'edit_form': edit_user_form}
    return render(request, 'account/edit_profile.html', context)


class AdminHome(AdminAccessMixin, ListView):
    queryset = Product.objects.all()
    template_name = 'myAdminPanel/home.html'


class ProductCreate(AdminAccessMixin, FieldsMixin, CreateView):
    model = Product
    template_name = 'myAdminPanel/product-create-update.html'


class ProductUpdate(AdminAccessMixin, FieldsMixin, UpdateView):
    model = Product
    template_name = 'myAdminPanel/product-create-update.html'


class ProductDelete(AdminAccessMixin,  DeleteView):
    model = Product
    success_url = reverse_lazy('account:home')
    template_name = 'myAdminPanel/product_confirm_delete.html'


class OrderView(AdminAccessMixin, ListView):
    queryset = Order.objects.filter(is_paid=True)
    template_name = 'myAdminPanel/order.html'


class OrderUpdate(AdminAccessMixin, UpdateView):
    model = Order
    fields = ['is_read']
    success_url = reverse_lazy('account:order')
    template_name = 'myAdminPanel/order_update.html'