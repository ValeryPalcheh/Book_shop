from django.urls import path
from book_shop_app import views


urlpatterns = [
    path('first-page-list/', views.FirstPageList.as_view()),
    path('book-list-classbv/', views.BookList.as_view()),
    path('book-list-det-classbv/<int:pk>/', views.BookListDetail.as_view()),
    path('book-create-classbv/', views.BookCreate.as_view()),
    path('book-update-classbv/<int:pk>/', views.BookUpdate.as_view()),
    path('book-delete-classbv/<int:pk>/', views.BookDelete.as_view()),
    path('author-list-classbv/', views.AuthorList.as_view()),
    path('author-list-det-classbv/<int:pk>/', views.AuthorListDetail.as_view()),
    path('author-create-classbv/', views.AuthorCreate.as_view()),
    path('author-update-classbv/<int:pk>/', views.AuthorUpdate.as_view()),
    path('author-delete-classbv/<int:pk>/', views.AuthorDelete.as_view()),
    path('series-list-classbv/', views.SeriesList.as_view()),
    path('series-list-det-classbv/<int:pk>/', views.SeriesListDetail.as_view()),
    path('series-create-classbv/', views.SeriesCreate.as_view()),
    path('series-update-classbv/<int:pk>/', views.SeriesUpdate.as_view()),
    path('series-delete-classbv/<int:pk>/', views.SeriesDelete.as_view()),
    path('genre-list-classbv/', views.GenreList.as_view()),
    path('genre-list-det-classbv/<int:pk>/', views.GenreListDetail.as_view()),
    path('genre-create-classbv/', views.GenreCreate.as_view()),
    path('genre-update-classbv/<int:pk>/', views.GenreUpdate.as_view()),
    path('genre-delete-classbv/<int:pk>/', views.GenreDelete.as_view()),
    path('publisher-list-classbv/', views.PublisherList.as_view()),
    path('publisher-list-det-classbv/<int:pk>/', views.PublisherListDetail.as_view()),
    path('publisher-create-classbv/', views.PublisherCreate.as_view()),
    path('publisher-update-classbv/<int:pk>/', views.PublisherUpdate.as_view()),
    path('publisher-delete-classbv/<int:pk>/', views.PublisherDelete.as_view()),


]
