# Generated by Django 5.0.7 on 2024-08-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_ordergoods'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergoods',
            name='address',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='tel',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='total_order_price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость заказа'),
        ),
    ]
