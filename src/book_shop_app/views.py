from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models, utils
from django.views import generic
# Create your views here.


class BookList(generic.ListView):
    model = models.Book

class BookListDetail(generic.DetailView):
    model = models.Book

class BookCreate(generic.CreateView):
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

class BookUpdate(generic.UpdateView):
    model = models.Book
    fields = ['title', 'cover', 'price', 'author', 'series', 'genre', 'publication_year', 'pages',
              'binding', 'format', 'isbn', 'weight', 'age_restrictions',
              'publisher', 'quantity_in_stock', 'is_active', 'rating',]

class BookDelete(generic.DeleteView):
    model = models.Book
    success_url = "/book-list-classbv/"

class AuthorList(generic.ListView):
    model = models.Author

class AuthorListDetail(generic.DetailView):
    model = models.Author

class AuthorCreate(generic.CreateView):
    model = models.Author
    fields = ['name', 'bio',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание нового автора:"
        return context

class AuthorUpdate(generic.UpdateView):
    model = models.Author
    fields = ['name', 'bio',]

class AuthorDelete(generic.DeleteView):
    model = models.Author
    success_url = "/author-list-classbv/"


class SeriesList(generic.ListView):
    model = models.Series

class SeriesListDetail(generic.DetailView):
    model = models.Series

class SeriesCreate(generic.CreateView):
    model = models.Series
    fields = ['title', 'description',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание новой серии:"
        return context

class SeriesUpdate(generic.UpdateView):
    model = models.Series
    fields = ['title', 'description',]

class SeriesDelete(generic.DeleteView):
    model = models.Series
    success_url = "/series-list-classbv/"

class GenreList(generic.ListView):
    model = models.Genre

class GenreListDetail(generic.DetailView):
    model = models.Genre

class GenreCreate(generic.CreateView):
    model = models.Genre
    fields = ['name',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание нового жанра:"
        return context

class GenreUpdate(generic.UpdateView):
    model = models.Genre
    fields = ['name',]

class GenreDelete(generic.DeleteView):
    model = models.Genre
    success_url = "/genre-list-classbv/"


class PublisherList(generic.ListView):
    model = models.Publisher

class PublisherListDetail(generic.DetailView):
    model = models.Publisher

class PublisherCreate(generic.CreateView):
    model = models.Publisher
    fields = ['name', 'address', 'website',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание нового издательства:"
        return context

class PublisherUpdate(generic.UpdateView):
    model = models.Publisher
    fields = ['name', 'address', 'website',]

class PublisherDelete(generic.DeleteView):
    model = models.Publisher
    success_url = "/publisher-list-classbv/"


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

