from django.contrib import admin

# Register your models here.
from .models import Product, IPAddress
admin.site.site_header = "پنل مدیریت سایت"

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'name_fa', 'year', 'price', 'discount', 'active']
    list_filter = ['categories', 'brands']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(IPAddress)