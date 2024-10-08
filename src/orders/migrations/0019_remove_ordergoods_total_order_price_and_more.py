# Generated by Django 5.0.7 on 2024-09-04 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_alter_orderstatus_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordergoods',
            name='total_order_price',
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='status_order',
            field=models.CharField(choices=[('ожидает обработки', 'ожидает обработки'), ('отправлен', 'отправлен'), ('доставлен', 'доставлен'), ('отменен', 'отменен')], default='ожидает обработки', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='status',
            field=models.CharField(choices=[('ожидает обработки', 'ожидает обработки'), ('отправлен', 'отправлен'), ('доставлен', 'доставлен'), ('отменен', 'отменен')], max_length=20),
        ),
    ]
