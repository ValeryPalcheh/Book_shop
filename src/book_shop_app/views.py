from django.shortcuts import render
from django.http import HttpResponse
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

