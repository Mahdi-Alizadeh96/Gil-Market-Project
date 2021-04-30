from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'name_fa', 'year', 'price', 'active']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
