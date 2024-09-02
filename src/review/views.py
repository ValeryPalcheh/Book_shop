from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import ReviewForm
from django.urls import reverse, reverse_lazy
from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            # return redirect('book-detail', book_id=book.id)
            return redirect(reverse_lazy('book_shop:book-list'))
    else:
        form = ReviewForm()

    context = {
        'book': book,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'review/book_detail.html', context)
    


class ReviewDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):      
    permission_required = 'review.delete_review'
    login_url = reverse_lazy('user:login')
    model = models.Review
    success_url = reverse_lazy('review:review-list')






class ReviewList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'review.view_review'
    login_url = reverse_lazy('user:login')
    model = models.Review
    paginate_by = 20