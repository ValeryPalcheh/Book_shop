from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def about(request):
    return HttpResponse("About us")


def book_list(request):
    books = models.Book.objects.all()
    context = {
        "object_list": books,
        "page_title": "books"
    }
    return render(
        request,
        template_name="book-list.html",
        context=context)

def book_list_det(request, book_id):
    book = models.Book.objects.get(pk=book_id)
    context = {
        'object': book,
        'page_title': f'Book {book.pk}'
    }
    return render(
        request,
        template_name="book-list-det.html",
        context=context)

def author_list(request):
    authors = models.Author.objects.all()
    context = {
        "object_list": authors,
        "page_title": "authors"
    }
    return render(
        request,
        template_name="author-list.html",
        context=context)

def author_det(request, author_id):
    author = models.Author.objects.get(pk=author_id)
    context = {
        'object': author,
        'page_title': f'Autror {author.pk}'
    }
    return render(
        request,
        template_name="author-det.html",
        context=context)

def book_create(request):
    if request.method == "GET":
        authors = models.Author.objects.all()
        context = {
            'page_title': f'Book create',
            'authors': authors
        }
        return render(
            request,
            template_name="book-create.html",
            context=context)
    if request.method == "POST":
        author_id = request.POST.get("author")
        author = models.Book.object.get(pk=author_id)
        title = request.POST.get("title")
        
        new_book = models.Book.objects.create(
            title=title,
            author=author
        )
        print(new_book)
        return HttpResponseRedirect(f"/book-list-det/{new_book.id}/")


