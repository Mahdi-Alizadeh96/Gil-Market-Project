import os

from django.db import models

from Gil_Products_Category.models import ProductCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.name_en}{ext}"
    return f"products/{final_name}"


class ProductManager(models.Manager):
    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_product_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name)


class Product(models.Model):
    name_fa = models.CharField(max_length=30, verbose_name='نام محصول (فارسی)')
    name_en = models.CharField(max_length=50, verbose_name='نام محصول (انگلیسی)')
    year = models.IntegerField(verbose_name='سال تولید')
    price = models.BigIntegerField(verbose_name='قیمت')
    discount = models.IntegerField(null=True, blank=True, verbose_name='مبلغ تخفیف')
    description = models.TextField(verbose_name='توضیحات محصول')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='موجود / ناموجود')
    categories = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True,
                                   verbose_name="دسته بندی ها")

    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name_en
