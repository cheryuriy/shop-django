# Generated by Django 2.0.3 on 2018-04-17 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20180417_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='ordered_product',
            name='order',
        ),
        migrations.RemoveField(
            model_name='ordered_product',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Ordered_product',
        ),
    ]
