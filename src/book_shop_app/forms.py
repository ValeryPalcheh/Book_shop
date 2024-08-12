from django import forms
from . import models


class BookCreateForm(forms.ModelForm):
      
    class Meta:
        model = models.Book
        fields = ['title', 'cover', 'price', 'author', 'series', 'genre', 'publication_year', 'pages',
           'binding', 'format', 'isbn', 'weight', 'age_restrictions',
           'publisher', 'quantity_in_stock', 'is_active', 'rating',]
    
        


















    # title = forms.CharField(max_length=200, required=True, label='Название',)
    # cover = forms.ImageField(required=True, label='Обложка',)
    # price = forms.DecimalField(max_digits=10, decimal_places=2, required=True, label='Цена',)
    # author = forms.CharField(required=True, label='Автор', )
    # series = forms.CharField(required=True, label='Серия',)
    # genre = forms.CharField(required=True, label='Жанр',)
    # publication_year = forms.CharField(required=True, label='Год издания',)
    # pages = forms.CharField(required=True, label='Количество страниц',)
    # binding = forms.CharField(max_length=50, required=True, label='Переплет',)
    # format = forms.CharField(max_length=50, required=True, label='Формат',)
    # isbn = forms.CharField(max_length=13, required=True, label='ISBN',)
    # weight = forms.FloatField(required=True, label='Вес книги',)
    # age_restrictions = forms.CharField(max_length=50, required=True, label='Возврастные ограничения',)
    # publisher = forms.CharField(required=True, label='Издательство',)
    # quantity_in_stock = forms.CharField(required=True, label='Количество книг в наличии',)
    # is_active = forms.BooleanField(required=True, label='Доступен для заказа',)
    # rating = forms.FloatField(required=True, label='Рейтинг книги',)