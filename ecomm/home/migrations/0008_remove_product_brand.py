# Generated by Django 4.1.1 on 2022-09-20 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
    ]
