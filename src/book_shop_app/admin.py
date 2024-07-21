from django.contrib import admin
from book_shop_app.models import Publisher, Genre, Author, Series, Book

admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Book)

