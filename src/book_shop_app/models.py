from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Series(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='covers/')  # Папка для изображений обложек
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена книги
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publication_year = models.PositiveIntegerField()  # Год издания
    pages = models.PositiveIntegerField()  # Количество страниц
    binding = models.CharField(max_length=50)  # Переплет (мягкий, твердый и т.д.)
    format = models.CharField(max_length=50)  # Формат (например, A5, A4 и т.д.)
    isbn = models.CharField(max_length=13, unique=True)  # ISBN
    weight = models.FloatField()  # Вес книги (например, в граммах)
    age_restrictions = models.CharField(max_length=50, blank=True)  # Возрастные ограничения
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    quantity_in_stock = models.PositiveIntegerField(default=0)  # Количество книг в наличии
    is_active = models.BooleanField(default=True)  # Доступен для заказа
    rating = models.FloatField(default=0.0)  # Рейтинг книги
    date_added = models.DateTimeField(auto_now_add=True)  # Дата внесения в каталог
    last_modified = models.DateTimeField(auto_now=True)  # Дата последнего изменения карточки

    def __str__(self):
        return self.title

"""
db.sqlite3
Описание полей:
title: Название книги.
cover_image: Изображение обложки, загружается в папку covers/.
price: Цена книги с двумя знаками после запятой.
author: Связь с моделью Author, указывающая автора книги.
series: Связь с моделью Series, указывающая серию книги, может быть пустым.
genre: Связь с моделью Genre, указывающая жанр книги.
publication_year: Год издания книги (целое число).
pages: Количество страниц в книге (целое число).
binding: Вид переплета книги (строка).
format: Формат книги (строка).
isbn: Международный стандартный книжный номер, уникальный для каждой книги.
weight: Вес книги в граммах (число с плавающей точкой).
age_restrictions: Возрастные ограничения для книги (строка).
publisher: Связь с моделью Publisher, указывающая издательство.
quantity_in_stock: Количество книг в наличии (целое число).
is_active: Флаг доступности книги (логическое значение, по умолчанию — True).
rating: Рейтинг книги (число с плавающей точкой, по умолчанию 0.0).
date_added: Дата добавления книги в каталог (автоматически устанавливается при создании).
last_modified: Дата последнего изменения карточки книги (автоматически обновляется).
Обратите внимание:
Не забудьте добавить соответствующие настройки для работы с изображениями в файле settings.py, указав MEDIA_URL и MEDIA_ROOT.
"""












# class Publisher(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.TextField(blank=True)  # Адрес может быть необязательным полем.
#     website = models.URLField(blank=True)   # Сайт издательства может быть необязательным.

#     def __str__(self):
#         return self.name


# class Genre(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Author(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     bio = models.TextField(blank=True)  # Биография может быть необязательной.

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


# class Series(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)  # Описание серии может быть необязательным.

#     def __str__(self):
#         return self.title


# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
#     series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True, null=True)  # Серия может быть необязательной.
#     publication_date = models.DateField()

#     def __str__(self):
#         return self.title











# class Directory(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(
#         blank=True,
#         null=True
#     )
#     def __str__(self):
#         return f"{self.name} # {self.pk}"
    
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     directory = models.ForeignKey(
#         Directory,
#         on_delete=models.PROTECT,
#         related_name="authors"
#     )
#     def __str__(self):
#         return f"{self.name} # {self.pk}"
    
# class Genre(models.Model):
#     name = models.CharField(max_length=100)
#     directory = models.ForeignKey(
#         Directory,
#         on_delete=models.PROTECT,
#         related_name="genres"
#     )
#     def __str__(self):
#         return f"{self.name} # {self.pk}"
    
# class Publishing_house(models.Model):
#     name = models.CharField(max_length=100)
#     directory = models.ForeignKey(
#         Directory,
#         on_delete=models.PROTECT,
#         related_name="publishing_houses"
#     )
#     def __str__(self):
#         return f"{self.name} # {self.pk}" 
# class Series(models.Model):
#     name = models.CharField(max_length=100)
#     directory = models.ForeignKey(
#         Directory,
#         on_delete=models.PROTECT,
#         related_name="series"
#     )   
#     def __str__(self):
#         return f"{self.name} # {self.pk}"
    