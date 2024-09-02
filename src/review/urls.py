
from django.urls import path, include
from . views import book_detail
from . import views

app_name = "review"

urlpatterns = [  
    path('book/<int:book_id>/', book_detail, name='book-detail'),
    path('review-list/', views.ReviewList.as_view(), name="review-list"),
    path('review-delete/<int:pk>/', views.ReviewDelete.as_view(), name="review-delete"),
]