from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "book_shop"

urlpatterns = [
    path('first-page/', views.FirstPageList.as_view(), name="first-page"),
    path('search/', views.search, name='search'),    
    path('book-list/', views.BookList.as_view(), name="book-list"),
    path('book-detail/<int:pk>/', views.BookListDetail.as_view(), name="book-detail"),
    path('book-create/', views.BookCreate.as_view(), name="book-create"),
    path('book-update/<int:pk>/', views.BookUpdate.as_view(), name="book-update"),
    path('book-delete/<int:pk>/', views.BookDelete.as_view(), name="book-delete"),
    path('author-list/', views.AuthorList.as_view(), name="author-list"),
    path('author-detail/<int:pk>/', views.AuthorListDetail.as_view(), name="author-detail"),
    path('author-create/', views.AuthorCreate.as_view(), name="author-create"),
    path('author-update/<int:pk>/', views.AuthorUpdate.as_view(), name="author-update"),
    path('author-delete/<int:pk>/', views.AuthorDelete.as_view(), name="author-delete"),
    path('series-list/', views.SeriesList.as_view(), name="series-list"),
    path('series-detail/<int:pk>/', views.SeriesListDetail.as_view(), name="series-detail"),
    path('series-create/', views.SeriesCreate.as_view(), name="series-create"),
    path('series-update/<int:pk>/', views.SeriesUpdate.as_view(), name="series-update"),
    path('series-delete/<int:pk>/', views.SeriesDelete.as_view(), name="series-delete"),
    path('genre-list/', views.GenreList.as_view(), name="genre-list"),
    path('genre-detail/<int:pk>/', views.GenreListDetail.as_view(), name="genre-detail"),
    path('genre-create/', views.GenreCreate.as_view(), name="genre-create"),
    path('genre-update/<int:pk>/', views.GenreUpdate.as_view(), name="genre-update"),
    path('genre-delete/<int:pk>/', views.GenreDelete.as_view(), name="genre-delete"),
    path('publisher-list/', views.PublisherList.as_view(), name="publisher-list"),
    path('publisher-detail/<int:pk>/', views.PublisherListDetail.as_view(), name="publisher-detail"),
    path('publisher-create/', views.PublisherCreate.as_view(), name="publisher-create"),
    path('publisher-update/<int:pk>/', views.PublisherUpdate.as_view(), name="publisher-update"),
    path('publisher-delete/<int:pk>/', views.PublisherDelete.as_view(), name="publisher-delete"),
]
