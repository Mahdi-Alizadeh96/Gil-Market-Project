from django.db import models

from Gil_Products.models import Product
from base_user_account.models import User
from extensions.utils import jalali_converter

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نام خریدار')
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده / نشده')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):
        return self.owner.get_full_name()

    def get_total_price(self):
        total = 0
        for detail in self.orderdetail_set.all():
            total += detail.product.get_sale()
        return total
    
    def jpayment_date(self):
        return jalali_converter(self.payment_date)
    jpayment_date.short_description = 'تاریخ پرداخت'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    count = models.IntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'اطلاعات جزییات سبدهای خرید'

    def __str__(self):
        return self.product.name_fa
