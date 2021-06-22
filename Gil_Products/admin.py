from django.contrib import admin

# Register your models here.
from .models import Product, Gallery
admin.site.site_header = "پنل مدیریت سایت"

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'name_fa', 'year', 'price', 'discount', 'active']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Gallery)
