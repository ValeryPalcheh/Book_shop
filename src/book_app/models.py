from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(
        verbose_name='Item title',
        max_length=200
    )
    cover = models.ImageField(
        verbose_name='Item cover',
        upload_to='item_covers/%Y/%m/%d'
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return ''

