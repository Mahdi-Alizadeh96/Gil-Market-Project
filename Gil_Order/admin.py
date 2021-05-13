from django.contrib import admin

# Register your models here.
from .models import Order, OrderDetail

admin.site.register(Order)
admin.site.register(OrderDetail)
