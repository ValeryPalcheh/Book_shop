from django.db import models
from django.contrib.auth import get_user_model # вместо user

User = get_user_model()

# class Cart(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         related_name='carts',
#         blank=True,       # пусто из-за ананимного пользователя
#         null=True         # пусто из-за ананимного пользователя
#     )
#     created = models.DateTimeField(
#         verbose_name="Дата создания",
#         auto_now_add=True,
#         auto_now=False,
#     )
#     updated = models.DateTimeField(
#         verbose_name="Дата изменения",
#         auto_now_add=False,
#         auto_now=True,
#     )

#     @property
#     def order_price(self):
#         books = self.books.all()
#         total_order_price = 0
#         for book in books:
#             total_order_price += book.price
#         return total_order_price

#     def __str__(self) -> str:
#         return f'Корзина: {self.pk} - для {self.user}'


# class BookInCart(models.Model):
#     cart = models.ForeignKey(
#         Cart,
#         on_delete=models.PROTECT,
#         verbose_name="Корзина",
#         related_name="books",
#     )
#     book = models.ForeignKey(
#         "book_shop_app.Book",
#         on_delete=models.PROTECT,
#         verbose_name="Книга",
#         related_name="books_in_cart",
#     )
#     quantity = models.IntegerField(
#         verbose_name="Количество",
#         default=1
#     )
#     price_per_book = models.DecimalField(
#         verbose_name="Цена за книгу",
#         max_digits=7,
#         decimal_places=2,
#     )
#     @property
#     def price(self):
#         return self.quantity * self.price_per_book

#     def __str__(self) -> str:
#         return f"Книга {self.book.pk} в корзине {self.cart.pk}, количество {self.quantity}"
    

