from django.db import models

from Gil_Products.models import Product


class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', null=True,
                                verbose_name='نام محصول')
    name = models.CharField(max_length=150, verbose_name="نام کاربر")
    message = models.TextField(verbose_name='متن پیام')
    postedTime = models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال')
    active = models.BooleanField(default=False, verbose_name='نمایش / عدم نمایش')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.name
