# Generated by Django 3.1.7 on 2021-06-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_user_account', '0004_auto_20210625_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=350, null=True, unique=True, verbose_name='آدرس'),
        ),
    ]
