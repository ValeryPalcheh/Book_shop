
from django.urls import path, include
from . import views

app_name = "user"

urlpatterns = [   
    path('login/', views.MyLoginView.as_view(), name="login"),   
]