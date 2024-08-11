from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms, utils
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy

# Create your views here.


class BookList(generic.ListView):
    model = models.Book

class BookListDetail(generic.DetailView):
    model = models.Book

class BookCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_book'
    login_url = reverse_lazy('user:login')
    model = models.Book
    fields = ['title', 'cover', 'price', 'author', 'series', 'genre', 'publication_year', 'pages',
              'binding', 'format', 'isbn', 'weight', 'age_restrictions',
              'publisher', 'quantity_in_stock', 'is_active', 'rating',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание новой книги:"
        return context
    # отправка по эл.почтe о заказе менеджеру
    # def get_success_url(self) -> str:
    #     url = super().get_success_url()
    #     utils.send_email(address=manager_address, text=f'Order # {self.object.pk} was created')
    #     return url

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


class AuthorListDetail(generic.DetailView): 
    model = models.Author

class AuthorCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_author' 
    login_url = reverse_lazy('user:login')
    model = models.Author
    
    fields = ['name', 'bio',]

    # def test_func(self):
    #     if self.request.user.username == 'Manager':
    #         return True
    #     else:
    #         return False
    
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



















# def book_list(request):
#     books = models.Book.objects.all()
#     context = {
#         "object_list": books,
#         "page_title": "books"
#     }
#     return render(
#         request,
#         template_name="book-list.html",
#         context=context)


# def book_list_det(request, book_id):
#     book = models.Book.objects.get(pk=book_id)
#     context = {
#         'object': book,
#         'page_title': f'Book {book.pk}'
#     }
#     return render(
#         request,
#         template_name="book-list-det.html",
#         context=context)

# def book_create(request):
#     if request.method == "GET":
#         authors = models.Author.objects.all()
#         context = {
#             'page_title': f'Book create',
#             'authors': authors
#         }
#         return render(
#             request,
#             template_name="book-create.html",
#             context=context)
#     if request.method == "POST":
#         author_id = request.POST.get("author")
#         author = models.Book.object.get(pk=author_id)
#         title = request.POST.get("title")
        
#         new_book = models.Book.objects.create(
#             title=title,
#             author=author
#         )
#         print(new_book)
#         return HttpResponseRedirect(f"/book-list-det/{new_book.id}/")

# def author_list(request):
#     authors = models.Author.objects.all()
#     context = {
#         "object_list": authors,
#         "page_title": "authors"
#     }
#     return render(
#         request,
#         template_name="author-list.html",
#         context=context)

# def author_det(request, author_id):
#     author = models.Author.objects.get(pk=author_id)
#     context = {
#         'object': author,
#         'page_title': f'Autror {author.pk}'
#     }
#     return render(
#         request,
#         template_name="author-det.html",
#         context=context)

# def index(request):
#     return HttpResponse("Hello, world!")

# def about(request):
#     return HttpResponse("About us")

