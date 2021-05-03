import os

from django.db import models

from Gil_Products_Category.models import ProductCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"brand/{final_name}"


class ProductBrandManager(models.Manager):
    def get_by_name(self, brand_name):
        qs = self.get_queryset().filter(name__iexact=brand_name)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class ProductBrand(models.Model):
    title = models.CharField(max_length=150, verbose_name='نام برند')
    name = models.CharField(max_length=150, verbose_name='عنوان در URL')
    description = models.TextField(verbose_name='توضیحات برند')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی ها')

    objects = ProductBrandManager()

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    def __str__(self):
        return self.title
