from django.db import models
from django.urls import reverse, reverse_lazy

class Author(models.Model):
    name = models.CharField(verbose_name='ФИО автора', max_length=100)
    bio = models.TextField(verbose_name='Краткая биография автора', blank=True)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
       return reverse_lazy('book_shop:author-detail', kwargs={"pk": self.pk}) 

class Series(models.Model):
    title = models.CharField(verbose_name='Серия', max_length=100)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('book_shop:series-detail', kwargs={"pk": self.pk})

class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('book_shop:genre-detail', kwargs={"pk": self.pk})

class Publisher(models.Model):
    name = models.CharField(verbose_name='Название издательства', max_length=255)
    address = models.TextField(verbose_name='Адрес издательства', blank=True)
    website = models.URLField(verbose_name='Вебсайт издательства', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('book_shop:publisher-detail', kwargs={"pk": self.pk})

class Book(models.Model):
    title = models.CharField(verbose_name='Название книги', max_length=200)
    cover = models.ImageField(verbose_name='Обложка', upload_to='book_covers/%Y/%m/%d')  # Папка для изображений обложек
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)  # Цена книги
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.CASCADE, related_name="authors")
    series = models.ForeignKey(Series, verbose_name='Серия', on_delete=models.CASCADE, blank=True, null=True, related_name="series")
    genre = models.ForeignKey(Genre, verbose_name='Жанр', on_delete=models.CASCADE, related_name="genres")
    publication_year = models.PositiveIntegerField(verbose_name='Год издания')  # Год издания
    pages = models.PositiveIntegerField(verbose_name='Количество страниц')  # Количество страниц
    binding = models.CharField(verbose_name='Переплет', max_length=50)  # Переплет (мягкий, твердый и т.д.)
    format = models.CharField(verbose_name='Формат', max_length=50)  # Формат (например, A5, A4 и т.д.)
    isbn = models.CharField( verbose_name='Международный стандартный книжный номер (ISBN)', max_length=13, unique=True)  # ISBN
    weight = models.FloatField(verbose_name='Вес книги')  # Вес книги
    age_restrictions = models.CharField(verbose_name='Возрастные ограничения', max_length=50, blank=True)  # Возрастные ограничения
    publisher = models.ForeignKey(Publisher, verbose_name='Издательство', on_delete=models.CASCADE, related_name="publishers")
    quantity_in_stock = models.PositiveIntegerField(verbose_name='Количество книг в наличии', default=0)  # Количество книг в наличии
    is_active = models.BooleanField(verbose_name='Доступен для заказа', default=True)  # Доступен для заказа
    rating = models.FloatField(verbose_name='Рейтинг книги', default=0.0)  # Рейтинг книги
    date_added = models.DateTimeField(verbose_name='Дата внесения в каталог', auto_now_add=True)  # Дата внесения в каталог
    last_modified = models.DateTimeField(verbose_name='Дата последнего изменения карточки', auto_now=True)  # Дата последнего изменения карточки

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('book_shop:book-detail', kwargs={"pk": self.pk})



class FirstPage(models.Model):
    pass


