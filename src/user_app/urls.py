
from django.urls import path, include
from . import views
from . views import registration

app_name = "user"

urlpatterns = [  
    path('registration/', registration, name="registration"), 
    path('login/', views.MyLoginView.as_view(), name="login"),   
    path('profile-detail/', views.CustomerDetail.as_view(), name="profile-detail"), 
    path('profile-create/', views.CustomerCreate.as_view(), name="profile-create"),
]