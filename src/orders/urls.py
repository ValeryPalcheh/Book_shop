
from django.urls import path, include
from . import views

app_name = "orders"

urlpatterns = [  
    path("cart/", views.view_cart, name="view-cart"),
    path("add-item/", views.add_item_to_cart_view, name="add-item-to-cart"),
    path("evaluate/", views.evaluate_cart, name="evaluate-cart"),
    path("order-create/", views.CreateOrderGoodsView.as_view(), name="view-order-create"),
    path("created/", views.OrderGoodsCreateView.as_view(), name="created-page"),
    path('order-goods-list/', views.OrderGoodsList.as_view(), name="order-goods-list"),
    ]