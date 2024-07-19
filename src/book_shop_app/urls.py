from django.urls import path
from book_shop_app import views
# from book_shop_app.views import user_form
# from book_shop_app.views import add_user

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('user/', user_form, name='user_form'),
    # path('user/add', add_user, name='add_user'),
]
