# Generated by Django 5.0.7 on 2024-07-19 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover_image', models.ImageField(upload_to='covers/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('publication_year', models.PositiveIntegerField()),
                ('pages', models.PositiveIntegerField()),
                ('binding', models.CharField(max_length=50)),
                ('format', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('weight', models.FloatField()),
                ('age_restrictions', models.CharField(blank=True, max_length=50)),
                ('quantity_in_stock', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('rating', models.FloatField(default=0.0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop_app.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Directory',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop_app.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop_app.publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book_shop_app.series'),
        ),
    ]
