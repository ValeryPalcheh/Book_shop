from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from . import models, forms
from book_shop_app.models import Book
from user_app.models import Customer
from orders.models import Cart, OrderGoods, OrderStatus
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404


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
        # сделать ограничение на созд пустого заказа
        
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


#  достать usera
def get_create_user(user):
    if not user.is_authenticated:
        user = None
    else:
        user = user
    return user


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
    model = models.OrderGoods, Cart
    form_class = forms.CreateOrderGoodsForm
    template_name = "orders/create_order.html"   
    success_url = reverse_lazy('orders:created-page')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = get_current_cart(self.request)
        return context
    
    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        form.fields['user'].initial = get_create_user(self.request.user)
        form.fields['tel'].initial = get_customer_tel(self.request.user)
        form.fields['address'].initial = get_customer_address(self.request.user)
        return form
        
            
    
    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id', None)

        try:
            ordergoods = models.OrderGoods.objects.get(cart=cart_id) 
            return  HttpResponseRedirect(reverse_lazy('orders:created-page'))
          
        except models.OrderGoods.DoesNotExist:
            ordergoods = form.save(commit=False)
            ordergoods.cart = get_current_cart(self.request)
            ordergoods.save()
            self.object = ordergoods
            # print('new')
            return HttpResponseRedirect(self.get_success_url())

            

#  просм созданный заказ
def view_order_cart(request):
    # cart = get_or_create_current_cart(request)        # корзина будет создаваться без товара
    cart = get_current_cart(request)                    # 
    context = {'cart': cart}    
    return render(
        request,
        template_name='orders/cart_list.html',
        context=context
    )




# 14 
class OrderGoodsCreateView(generic.TemplateView):
    model = models.OrderGoods
    template_name = "orders/create_page.html"



class OrderGoodsCreateViewNew(generic.ListView):
    model = models.OrderGoods
    template_name = "orders/create_new.html"


class OrderGoodsList(generic.ListView):
    model = models.OrderGoods
    paginate_by = 10


class OrderGoodsListDetail(generic.DetailView):
    model = models.OrderGoods
    

class OrderGoodsUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):     #LoginRequiredMixin, PermissionRequiredMixin, 
    permission_required = 'orders.change_ordergoods'
    login_url = reverse_lazy('user:login')
    model = models.OrderGoods
    fields = ['user', 'tel', 'address', ]

class OrderGoodsDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView): #LoginRequiredMixin, PermissionRequiredMixin, 
    permission_required = 'orders.delete_ordergoods'
    login_url = reverse_lazy('user:login')
    model = models.OrderGoods
    success_url = reverse_lazy('orders:order-goods-list')



class ItemInCartList(generic.ListView):
    model = models.ItemInCart
    paginate_by = 20


class ItemInCartDetail(generic.DetailView):
    model = models.ItemInCart

class ItemInCartDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):  #LoginRequiredMixin, PermissionRequiredMixin, 
    permission_required = 'orders.delete_itemincart'
    login_url = reverse_lazy('user:login')
    model = models.ItemInCart
    success_url = reverse_lazy('orders:item-in-cart-list')






class CartList(generic.ListView):
    model = models.Cart
    paginate_by = 20

class CartListDetail(generic.DetailView):
    model = models.Cart





class OrderStatusList(generic.ListView):
    model = OrderStatus
    paginate_by = 20

class OrderStatusDetail(generic.DetailView):
    model = OrderStatus


class OrderStatusCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):       #LoginRequiredMixin, PermissionRequiredMixin, 
    #permission_required = 'book_shop_app.add_publisher'
    #login_url = reverse_lazy('user:login')
    model = models.OrderStatus
    fields = ['ordergoods', 'status',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание статуса:"
        return context


class OrderStatusUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):          #LoginRequiredMixin, PermissionRequiredMixin, 
    permission_required = 'orders.change_orderstatus'
    login_url = reverse_lazy('user:login')
    model = models.OrderStatus
    fields = ['ordergoods', 'status',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Изменение статуса:"
        return context


class OrderStatusDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):  #LoginRequiredMixin, PermissionRequiredMixin, 
    permission_required = 'orders.delete_orderstatus'
    login_url = reverse_lazy('user:login')
    model = models.OrderStatus
    success_url = reverse_lazy('orders:order-status-list')




def order_status_list(request):
    if request.user.is_anonymous:
        user = None                 
    else:
        user = request.user   
    # Получаем все заказы и их статусы для текущего пользователя
    ordergoodss = OrderGoods.objects.filter(user=user).prefetch_related('statuses')
    return render(request, 'orders/order_status_list.html', {'ordergoodss': ordergoodss})






