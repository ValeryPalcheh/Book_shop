# Generated by Django 5.0.7 on 2024-09-02 06:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_itemincart_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemincart',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
