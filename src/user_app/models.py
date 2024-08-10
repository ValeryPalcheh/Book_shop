# vetca chernovik
from django.urls import reverse, reverse_lazy
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model # вместо user

User = get_user_model()
class Customer(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(max_length=300, null=True)
    additional_info = models.TextField(blank=True)
    # Поле для группы, которое не доступно к редактированию
    GROUP_CHOICES = [
        ('regular', 'Обычный покупатель'),
        ('vip', 'VIP покупатель'),
    ]
    group = models.CharField(max_length=10, choices=GROUP_CHOICES, default='regular')
    
    def __str__(self):
        return f"{self.user}"
    


class PersonalPage(models.Model):
    pass

