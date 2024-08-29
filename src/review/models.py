from django.db import models
from book_shop_app.models import Book
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
# User = get_user_model()
# Create your models here.

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    # user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='users')
    user_name = models.CharField(verbose_name='Имя',max_length=100)
    rating = models.PositiveIntegerField(verbose_name='рейтинг')
    comment = models.TextField(verbose_name='комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв от {self.user_name} на {self.book.title}'
  