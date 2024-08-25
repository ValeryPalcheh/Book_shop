from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from . import models, forms
from book_shop_app.models import Book
from user_app.models import Customer
from django.urls import reverse, reverse_lazy


# 4  получить_или_создать_текущую_корзину (сохраняем в сессии)
def get_or_create_current_cart(request):
    cart_id = request.session.get('cart_id', None) # проверка в сессии ID корзинки
    if request.user.is_anonymous:
        user = None                 # если анонимный, заменяем юзера на None
    else:
        user = request.user
    cart, created = models.Cart.objects.get_or_create(     
        pk=cart_id,
        defaults={'user': user},
    )                                 # берём объект, если нет то создаем; ищем по pk
    if created:
        request.session["cart_id"] = cart.pk # создаем в сессии ID корзины
    return cart
    

# 5   получить_текущую_корзину, создать при добавл товара
def get_current_cart(request):
    cart_id = request.session.get('cart_id', None)
    cart = models.Cart.objects.filter(pk=cart_id)
    if cart:
        cart = cart[0]
    else:
        cart = bool(cart)
    return cart


# 7  добавление товара в корзину
def add_item_to_cart(request):
    item_id = int(request.POST.get("item_id"))
    book = Book.objects.get(pk=item_id)
    price = book.price
    quantity = int(request.POST.get("quantity"))
    cart = get_or_create_current_cart(request)
    item_in_cart, created = models.ItemInCart.objects.get_or_create(
        cart=cart,
        item=book,
        defaults={
            "quantity": quantity,
            "price_per_item": price
        },
    )
    if not created: # если товар был, то нужно обновить количество
        current_quality = item_in_cart.quantity
        item_in_cart.quantity = current_quality + quantity
        item_in_cart.save()


# 8   изменение в корзине количества
def evaluate_cart(request):
    if request.method == "POST":
        # print(request.POST)
        action = None
        for key, value in request.POST.items():
            # print(key, value)   
            if key[0:4] == "quan":
                update_item_in_cart(key, value)
            if key[0:4] == "acti":
                action = value
        if action == "update":
            return HttpResponseRedirect(reverse_lazy("orders:view-cart"))
        # create_order()   # создать заказ
        return HttpResponseRedirect(reverse_lazy("orders:view-order-create"))




# 9 обновление корзины
def update_item_in_cart(key, quantity):
    item_in_cart_id = int(key.split(".")[1])
    item_in_cart = models.ItemInCart.objects.get(pk=item_in_cart_id)
    if int(quantity) == 0:
        item_in_cart.delete()
    else:
        item_in_cart.quantity = int(quantity)
        item_in_cart.save()



# 10 # создать заказ
# def create_order():
    # cart = get_current_cart(request)
    # pass


# 12 достать телефон покупателя
def get_customer_tel(user):
    if not user.is_authenticated:
        tel = None    
    else:       
        tel = user.profile.phone
    return tel



# 13 достать адрес покупателя
def get_customer_address(user):
    if not user.is_authenticated:
        address = None
    else:
        address = user.profile.address
    return address



# 2 просм корзины
def view_cart(request):
    # cart = get_or_create_current_cart(request)        # корзина будет создаваться без товара
    cart = get_current_cart(request)                    # 
    context = {'cart': cart}    
    return render(
        request,
        template_name='orders/view_cart.html',
        context=context
    )


# 3 функция созд запроса для добавл книги(товара):
def add_item_to_cart_view(request):
    if request.method == "POST":
        add_item_to_cart(request)
        #item_id = request.POST.get("item_id")
        #quantity = request.POST.get("quantity")
        
    return HttpResponseRedirect(reverse_lazy("orders:view-cart"))


# 10 # создать заказ
class CreateOrderGoodsView(generic.CreateView):
    model = models.OrderGoods
    form_class = forms.CreateOrderGoodsForm
    template_name = "orders/create_order.html"
    success_url = reverse_lazy('orders:created-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = get_current_cart(self.request)
        return context
    
    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        form.fields['tel'].initial = get_customer_tel(self.request.user)
        form.fields['address'].initial = get_customer_address(self.request.user)
        return form
    
    def form_valid(self, form):
        ordergoods = form.save(commit=False)
        ordergoods.cart = get_current_cart(self.request)
        ordergoods.save()
        self.object = ordergoods
        return HttpResponseRedirect(self.get_success_url())


# 14 
class OrderGoodsCreateView(generic.TemplateView):
    template_name = "orders/create.html"



class OrderGoodsList(generic.ListView):
    model = models.OrderGoods
    paginate_by = 20
    








