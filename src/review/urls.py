
from django.urls import path, include
from . views import book_detail

app_name = "review"

urlpatterns = [  
    path('book/<int:book_id>/', book_detail, name='book-detail'),
]