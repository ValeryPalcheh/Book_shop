# Generated by Django 5.0.7 on 2024-08-29 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_alter_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]