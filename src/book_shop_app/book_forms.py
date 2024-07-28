from django import forms
from . import models


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'cover', 'price', 'author', 'series', 'genre', 'publication_year', 'pages',
              'binding', 'format', 'isbn', 'weight', 'age_restrictions',
              'publisher', 'quantity_in_stock', 'is_active', 'rating',]
        







