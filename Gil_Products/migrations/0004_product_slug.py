# Generated by Django 3.1.7 on 2021-06-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gil_Products', '0003_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=None, max_length=100, unique=True, verbose_name='آدرس محصول'),
            preserve_default=False,
        ),
    ]