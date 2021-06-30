import os
from django.urls import reverse
from django.db.models import Q
from django.db import models
from Gil_Product_Brand.models import ProductBrand
from Gil_Products_Category.models import ProductCategory
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.name_en}{ext}".replace(' ', '-')
    return f"products/{final_name}"


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آدرس آی‌پی')


class ProductManager(models.Manager):
    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_product_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name)

    def get_product_by_category_brand(self, brand_name, category_name):
        return self.get_queryset().filter(brands__name__iexact=brand_name, categories__name__iexact=category_name)

    def search(self, query):
        lookup = Q(name_fa__icontains=query) | Q(name_en__icontains=query) | Q(description__icontains=query)
        return Product.objects.filter(lookup).distinct()


class Product(models.Model):
    name_fa = models.CharField(max_length=150, verbose_name='نام محصول (فارسی)')
    name_en = models.CharField(max_length=150, verbose_name='نام محصول (انگلیسی)')
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس محصول")
    year = models.IntegerField(verbose_name='سال تولید')
    price = models.BigIntegerField(verbose_name='قیمت')
    discount = models.IntegerField(null=True, blank=True, default=0, verbose_name='درصد تخفیف')
    description = models.TextField(verbose_name='توضیحات محصول')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر اصلی')
    image1 = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='1تصویر')
    image2 = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='2تصویر')
    image3 = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='3تصویر')
    image4 = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='4تصویر')
    active = models.BooleanField(default=True, verbose_name='موجود / ناموجود')
    categories = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name="دسته بندی ها")
    brands = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True, blank=True, verbose_name="برندها")
    attributes = models.TextField(verbose_name='ویژگی های محصول', null=True)
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, blank=True, related_name='hits', verbose_name='بازدیدها')

    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name_en

    def get_absolute_url(self):
        return reverse("account:home")

    def get_sale(self):
        price = int(self.price * (100 - self.discount) / 100)
        return price

    def p_url_name(self):
        return self.name_en.replace('/','-')

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)