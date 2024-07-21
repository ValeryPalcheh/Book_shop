from django.urls import path
from book_shop_app import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('book-list/', views.book_list, name='Все книги'),
    path('book-list-det/<int:book_id>/', views.book_list_det),
    path('author-list/', views.author_list, name='Все авторы'),
    path('author-det/<int:author_id>/', views.author_det),
    path('book-create/', views.book_create),
]
