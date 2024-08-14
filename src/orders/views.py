from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Create your views here.
from . import models
from book_shop_app.models import Book

# def update_book_in_cart(key, quantity):
#     book_in_cart_id = int(key.split(".")[1])
#     book_in_cart = models.BookInCart.objects.get(pk=book_in_cart_id)
#     if int(quantity) == 0:
#         book_in_cart.delete()
#     else:
#         book_in_cart.quantity = int(quantity)
#     book_in_cart.save()



# def get_or_create_current_cart(request):
#     cart_id = request.session.get('cart_id', None)
#     if request.user.is_anonymous:
#         user = None
#     else:
#         user = request.user
#     cart, created = models.Cart.objects.get_or_create(
#         pk=cart_id,
#         defaults={'user': user},
#     )
#     if created:
#         request.session["cart_id"] = cart.pk
#     return cart
    


# def create_order():
#     pass


# def get_current_cart(request):
#     cart_id = request.session.get('cart_id', None)
#     cart = models.Cart.objects.filter(pk=cart_id)
#     if cart:
#         cart = cart[0]
#     else:
#         cart = bool(cart)
#     return cart



# def add_book_to_cart(request):
#     book_id = request.POST.get("book_id")
#     book = Book.objects.get(pk=book_id)
#     # price = book.price
#     quantity = int(request.POST.get("quantity"))
#     cart = get_or_create_current_cart(request)
#     book_in_cart, created = models.BookInCart.objects.get_or_create(
#         cart=cart,
#         book=book,
#         defaults={
#             "quantity": quantity,
#             "price_per_book": book.price
#         },
#     )
#     if not created:
#         current_quality = book_in_cart.quantity
#         book_in_cart.quantity = current_quality + quantity
#         book_in_cart.save()



# def view_cart(request):
#     cart = get_current_cart(request)
#     context = {'cart': cart}
#     return render(
#         request,
#         template_name='orders/view_cart.html',
#         context=context
#     )



# def evaluate_cart(request):
#     if request.method == "POST":
#         print(request.POST)
#         # action = None
#         for key, value in request.POST.book():
#             print(key, value)
#         #     if key[0:4] == "quan":
#         #         update_book_in_cart(key, value)
#         #     if key[0:4] == "acti":
#         #         action = value
#         # if action == "update":
#     return HttpResponseRedirect(reverse_lazy("orders:view-cart"))
#         # create_order()
#         # return HttpResponseRedirect(reverse_lazy("orders:view-order-create"))



# def add_book_to_cart_view(request):
#     if request.method == "POST":
#         add_book_to_cart(request)   
#     return HttpResponseRedirect(reverse_lazy("orders:view-cart"))











