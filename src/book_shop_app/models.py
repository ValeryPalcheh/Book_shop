from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
#    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


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
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='covers/')  # Папка для изображений обложек
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена книги
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="authors")
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

#db.sqlite3