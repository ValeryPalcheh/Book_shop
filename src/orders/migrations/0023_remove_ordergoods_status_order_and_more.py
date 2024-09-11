# Generated by Django 5.0.7 on 2024-09-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_alter_orderstatus_ordergoods_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordergoods',
            name='status_order',
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='status',
            field=models.CharField(choices=[('ожидает обработки', 'ожидает обработки'), ('отправлен', 'отправлен'), ('доставлен', 'доставлен'), ('получен покупателем', 'получен покупателем'), ('отменен', 'отменен')], default='ожидает обработки', max_length=20, verbose_name='Статус'),
        ),
    ]