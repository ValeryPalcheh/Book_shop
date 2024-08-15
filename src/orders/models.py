from django.db import models
from django.contrib.auth import get_user_model # вместо user

User = get_user_model() # функция возвр текущую модель юзера в системе

# 1 созд корзину
class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,  # прежде чем удал юзера, будет требовать разобр с корзинами
        related_name='carts',
        blank=True,       # пусто из-за ананимного пользователя
        null=True         # пусто из-за ананимного пользователя
    )
    created = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,  # когда была создана
        auto_now=False,     # когда добавилась
    )
    updated = models.DateTimeField(
        verbose_name="Дата изменения",
        auto_now_add=False, # при добавлении не добавляем
        auto_now=True,      # добавляем при сохранении
    )

    @property
    def order_price(self):
        items = self.items.all()
        total_order_price = 0
        for item in items:
            total_order_price += item.price
        return total_order_price

    def __str__(self) -> str:
        return f'Корзина: {self.pk} - для {self.user}'


# 6  добавление товаров в корзину
class ItemInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        verbose_name="Корзина",
        related_name="items",
    )
    item = models.ForeignKey(
        "book_shop_app.Book",
        on_delete=models.PROTECT,
        verbose_name="Товар",
        related_name="items_in_cart",
    )
    quantity = models.IntegerField(
        verbose_name="Количество",
        default=1
    )
    price_per_item = models.DecimalField(
        verbose_name="Цена за товар",
        max_digits=7,
        decimal_places=2,
    )
    @property
    def price(self):
        return self.quantity * self.price_per_item

    def __str__(self) -> str:
        return f"Книга {self.item.pk} в корзине {self.cart.pk}, количество {self.quantity}"
    


# 11 мщдель заказ(новое)
class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_order_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'Заказ #{self.id} для корзины #{self.cart.id}'

