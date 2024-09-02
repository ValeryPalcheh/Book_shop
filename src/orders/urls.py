
from django.urls import path, include
from . import views

app_name = "orders"

urlpatterns = [  
    path("cart/", views.view_cart, name="view-cart"),
    path("cart-order-list/", views.view_order_cart, name="cart-order-list"),
    path("add-item/", views.add_item_to_cart_view, name="add-item-to-cart"),
    path("evaluate/", views.evaluate_cart, name="evaluate-cart"),
    path("order-create/", views.CreateOrderGoodsView.as_view(), name="view-order-create"),
    path("created-page/", views.OrderGoodsCreateView.as_view(), name="created-page"),
    path("created-new/", views.OrderGoodsCreateViewNew.as_view(), name="created-new"),
    path('order-goods-list/', views.OrderGoodsList.as_view(), name="order-goods-list"),
    path('orderdoods-detail/<int:pk>/', views.OrderGoodsListDetail.as_view(), name="orderdoods-detail"),
    path('item-in-cart-list/', views.ItemInCartList.as_view(), name="item-in-cart-list"),
    path('item-in-cart-detail/<int:pk>/', views.ItemInCartDetail.as_view(), name="item-in-cart-detail"),
    path('cart-list/', views.CartList.as_view(), name="cart-list"),
    path('cart-list-detail/<int:pk>/', views.CartListDetail.as_view(), name="cart-list-detail"),
    # path('order-goods-delete/<int:pk>/', views.OrderGoodsDelete.as_view(), name="order-goods-delete"),
    ]