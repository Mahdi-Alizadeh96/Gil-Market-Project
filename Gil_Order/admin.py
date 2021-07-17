from django.contrib import admin

# Register your models here.
from .models import Order, OrderDetail

class OrderAdmin(admin.ModelAdmin):
    list_display = ["__str__", "jpayment_date", "is_paid", "is_read"]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)
