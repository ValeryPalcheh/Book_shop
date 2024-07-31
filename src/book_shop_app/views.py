from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models, utils
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.


class BookList(PermissionRequiredMixin, generic.ListView):
    permission_required = 'book_shop_app.view_book'
    login_url = '/login'
    model = models.Book

class BookListDetail(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'book_shop_app.view_book'
    model = models.Book

class BookCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_book'
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

class BookUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'book_shop_app.change_book'
    model = models.Book
    fields = ['title', 'cover', 'price', 'author', 'series', 'genre', 'publication_year', 'pages',
              'binding', 'format', 'isbn', 'weight', 'age_restrictions',
              'publisher', 'quantity_in_stock', 'is_active', 'rating',]

class BookDelete(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'book_shop_app.delete_book'
    model = models.Book
    success_url = "/book-list-classbv/"







class AuthorList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'book_shop_app.view_author'
    login_url = '/login/'
    model = models.Author

class AuthorListDetail(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'book_shop_app.view_author'
    model = models.Author

class AuthorCreate(PermissionRequiredMixin, LoginRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_author' 
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

class AuthorUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'book_shop_app.change_author'
    model = models.Author
    fields = ['name', 'bio',]

class AuthorDelete(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'book_shop_app.delete_author'
    model = models.Author
    success_url = "/author-list-classbv/"








class SeriesList(PermissionRequiredMixin, generic.ListView):
    permission_required = 'book_shop_app.view_series'
    login_url = '/login'
    model = models.Series

class SeriesListDetail(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'book_shop_app.view_series'
    model = models.Series

class SeriesCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_series'
    model = models.Series
    fields = ['title', 'description',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание новой серии:"
        return context

class SeriesUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'book_shop_app.change_series'
    model = models.Series
    fields = ['title', 'description',]

class SeriesDelete(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'book_shop_app.delete_series'
    model = models.Series
    success_url = "/series-list-classbv/"









class GenreList(PermissionRequiredMixin, generic.ListView):
    permission_required = 'book_shop_app.view_genre'
    login_url = '/login'
    model = models.Genre

class GenreListDetail(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'book_shop_app.view_genre'
    model = models.Genre

class GenreCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_genre'
    model = models.Genre
    fields = ['name',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание нового жанра:"
        return context

class GenreUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'book_shop_app.change_genre'
    model = models.Genre
    fields = ['name',]

class GenreDelete(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'book_shop_app.delete_genre'
    model = models.Genre
    success_url = "/genre-list-classbv/"










class PublisherList(PermissionRequiredMixin, generic.ListView):
    permission_required = 'book_shop_app.view_publisher'
    login_url = '/login'
    model = models.Publisher

class PublisherListDetail(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'book_shop_app.view_publisher'
    model = models.Publisher

class PublisherCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'book_shop_app.add_publisher'
    model = models.Publisher
    fields = ['name', 'address', 'website',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание нового издательства:"
        return context

class PublisherUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'book_shop_app.change_publisher'
    model = models.Publisher
    fields = ['name', 'address', 'website',]

class PublisherDelete(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'book_shop_app.delete_publisher'
    model = models.Publisher
    success_url = "/publisher-list-classbv/"


class FirstPageList(generic.ListView):
    model = models.FirstPage


# class ForStaffList(generic.ListView):
#     model = models.ForStaff



























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

