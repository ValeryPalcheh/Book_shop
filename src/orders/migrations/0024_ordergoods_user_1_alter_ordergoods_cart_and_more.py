# Generated by Django 5.0.7 on 2024-09-04 12:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_remove_ordergoods_status_order_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergoods',
            name='user_1',
            field=models.CharField(default='', max_length=20, verbose_name='Покупатель_1'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='cart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='cart', to='orders.cart', verbose_name='Корзина'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
        ),
    ]
