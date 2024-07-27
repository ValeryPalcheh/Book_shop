# Generated by Django 5.0.7 on 2024-07-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Item title')),
                ('cover', models.ImageField(upload_to='', verbose_name='Item cover')),
            ],
        ),
    ]