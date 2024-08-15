from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Cart)
admin.site.register(models.ItemInCart)
admin.site.register(models.Order)  # новое