from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms, utils
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from .models import Book


def search(request):
    query = request.GET.get('q')
    book = models.Book.objects
    books = []
    if query:
        books = Book.objects.filter(title__icontains=query)  # Поиск по названию
    return render(request, 'book_shop_app/search_results.html', {'books': books, 'query': book})



class BookList(generic.ListView):
    model = models.Book
    paginate_by = 5

class BookListDetail(generic.DetailView):
    model = models.Book

class BookCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_book'
    login_url = reverse_lazy('user:login')
    model = models.Book
    form_class = forms.BookCreateForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание новой книги:"
        return context


class BookUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'book_shop_app.change_book'
    login_url = reverse_lazy('user:login')
    model = models.Book
    fields = ['title', 'cover', 'price', 'author', 'series', 'genre', 'publication_year', 'pages',
              'binding', 'format', 'isbn', 'weight', 'age_restrictions',
              'publisher', 'quantity_in_stock', 'is_active', 'rating',]

class BookDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'book_shop_app.delete_book'
    login_url = reverse_lazy('user:login')
    model = models.Book
    success_url = reverse_lazy('book_shop:book-list')






class AuthorList(generic.ListView): 
    model = models.Author
    paginate_by = 10

class AuthorListDetail(generic.DetailView): 
    model = models.Author

class AuthorCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_author' 
    login_url = reverse_lazy('user:login')
    model = models.Author
    
    fields = ['name', 'bio',]

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание нового автора:"
        return context

class AuthorUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'book_shop_app.change_author'
    login_url = reverse_lazy('user:login')
    model = models.Author
    fields = ['name', 'bio',]

class AuthorDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'book_shop_app.delete_author'
    login_url = reverse_lazy('user:login')
    model = models.Author
    success_url = reverse_lazy('book_shop:author-list')








class SeriesList(generic.ListView):   
    model = models.Series
    paginate_by = 10

class SeriesListDetail(generic.DetailView):    
    model = models.Series

class SeriesCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_series'
    login_url = reverse_lazy('user:login')
    model = models.Series
    fields = ['title', 'description',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание новой серии:"
        return context

class SeriesUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'book_shop_app.change_series'
    login_url = reverse_lazy('user:login')
    model = models.Series
    fields = ['title', 'description',]

class SeriesDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'book_shop_app.delete_series'
    login_url = reverse_lazy('user:login')
    model = models.Series
    success_url = reverse_lazy('book_shop:series-list')









class GenreList(generic.ListView):   
    model = models.Genre
    paginate_by = 10

class GenreListDetail(generic.DetailView):   
    model = models.Genre

class GenreCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_genre'
    login_url = reverse_lazy('user:login')
    model = models.Genre
    fields = ['name',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание нового жанра:"
        return context

class GenreUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'book_shop_app.change_genre'
    login_url = reverse_lazy('user:login')
    model = models.Genre
    fields = ['name',]

class GenreDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'book_shop_app.delete_genre'
    login_url = reverse_lazy('user:login')
    model = models.Genre
    success_url = reverse_lazy('book_shop:genre-list')









class PublisherList(generic.ListView):    
    model = models.Publisher
    paginate_by = 10

class PublisherListDetail(generic.DetailView):    
    model = models.Publisher

class PublisherCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_publisher'
    login_url = reverse_lazy('user:login')
    model = models.Publisher
    fields = ['name', 'address', 'website',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание нового издательства:"
        return context

class PublisherUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'book_shop_app.change_publisher'
    login_url = reverse_lazy('user:login')
    model = models.Publisher
    fields = ['name', 'address', 'website',]

class PublisherDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'book_shop_app.delete_publisher'
    login_url = reverse_lazy('user:login')
    model = models.Publisher
    success_url = reverse_lazy('book_shop:publisher-list')

class FirstPageList(generic.ListView):
    model = models.FirstPage
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['newest'] = get_item_for_today(self.request)
        # context['sale'] = get_item_on_sale(self.request)
        # context['top'] = get_top_item(self.request)
        return context





