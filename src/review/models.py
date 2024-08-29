from django.db import models
from book_shop_app.models import Book
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# User = get_user_model()
# Create your models here.



def validate_rating(value):
    if value > 10:
        raise ValidationError(
            '%(value)s превышает максимально допустимое значение 10',
            params={'value': value},
        )


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    # user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='users')
    user_name = models.CharField(verbose_name='Имя',max_length=100)
    rating = models.PositiveIntegerField(verbose_name='рейтинг', validators=[validate_rating], )
    comment = models.TextField(verbose_name='комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв от {self.user_name} на {self.book.title}'
  


