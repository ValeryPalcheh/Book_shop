from django.db import models
from django.contrib.auth import get_user_model # вместо user
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
        return f'№ {self.pk} ({self.user})'


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
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def price(self):
        return self.quantity * self.price_per_item

    def __str__(self) -> str:
        return f"корзина: {self.cart.pk}-товар: {self.id}, книга: {self.item.title},  количество: {self.quantity}"
    
    def get_creation_time(self):
        return self.created_at




#  11 мoдель заказ товара
class OrderGoods(models.Model):
    user = models.CharField(verbose_name='Покупатель', default='', max_length=20)
    cart = models.OneToOneField(Cart, on_delete=models.PROTECT, related_name='cart', verbose_name="Корзина")
    created_at = models.DateTimeField(auto_now_add=True)
    tel = models.CharField(verbose_name="Телефон", max_length=13)
    address = models.TextField(verbose_name="Адрес доставки", max_length=300, null=True)
    

    def __str__(self):
        return f'{self.cart}, заказ:{self.pk}'
    
    def get_absolute_url(self):
        return reverse_lazy('orders:orderdoods-detail', kwargs={"pk": self.pk})
    
# автоматич создается статус
@receiver(post_save, sender=OrderGoods)
def create_order_status(sender, instance, created, **kwargs):
    if created:
        OrderStatus.objects.create(ordergoods=instance)


class OrderStatus(models.Model):
    STATUS_CHOICES = [
        ('ожидает обработки', 'ожидает обработки'),
        ('отправлен', 'отправлен'),
        ('доставлен', 'доставлен'),
        ('товар получен', 'товар получен'),
        ('отменен', 'отменен'),
    ]

    ordergoods = models.ForeignKey(OrderGoods, verbose_name="Заказ покупателя", on_delete=models.PROTECT, related_name='statuses')
    status = models.CharField(verbose_name="Статус", default="ожидает обработки", max_length=20, choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}-{self.ordergoods}-{self.status}'

    def get_absolute_url(self):
        return reverse_lazy('orders:order-status-detail', kwargs={"pk": self.pk})
    



