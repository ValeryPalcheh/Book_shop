from django.db import models
from book_shop_app.models import Book
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
User = get_user_model()
# Create your models here.



def validate_rating(value):
    if value > 10:
        raise ValidationError(
            '%(value)s превышает максимально допустимое значение 10',
            params={'value': value},
        )

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(verbose_name='Имя',max_length=100, )
    rating = models.PositiveIntegerField(verbose_name='рейтинг', validators=[validate_rating], )
    comment = models.TextField(verbose_name='комментарий', max_length=200, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' от {self.user_name} на книгу "{self.book.title}"'
  
    def get_absolute_url(self):
        return reverse_lazy('review:review-detail', kwargs={"pk": self.pk})

