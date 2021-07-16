from django.urls import path

from .views import (
    login_user,
    register,
    log_out,
    user_panel,
    edit_profile,
    AdminHome,
    ProductCreate,
    ProductUpdate,
    ProductDelete,
    OrderView,
    OrderUpdate,
    OrderDetailView
)

app_name = 'account'
urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register, name='register'),
    path('log-out', log_out, name='log-out'),
    path('user', user_panel, name='user_panel'),
    path('user/edit', edit_profile, name='edit_profile'),
    
    path('account/', AdminHome.as_view(), name='home'),
    path('account/product/create', ProductCreate.as_view(), name='product-create'),
    path('account/product/update/<int:pk>', ProductUpdate.as_view(), name='product-update'),
    path('account/product/delete/<int:pk>', ProductDelete.as_view(), name='product-delete'),
    path('account/order', OrderView.as_view(), name='order'),
    path('account/order/update/<int:pk>', OrderUpdate.as_view(), name='order-update'),
    path('account/order-detail/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
]
