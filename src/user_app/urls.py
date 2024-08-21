
from django.urls import path, include
from . import views
from . views import registration, login_view, logout_view

app_name = "user"

urlpatterns = [  
    path("login_entrance/", login_view, name="login_entrance"),
    path("logout/", logout_view, name="logout"),
    path('registration/', registration, name="registration"), 
    path('login/', views.MyLoginView.as_view(), name="login"),
    path("personal-page-list/", views.PersonalPageList.as_view(), name="personal-page-list"), 
    path('profile-detail/', views.CustomerDetail.as_view(), name="profile-detail"), 
    path('profile-create/', views.CustomerCreate.as_view(), name="profile-create"),
    path('profile-update/<int:pk>/', views.CustomerUpdate.as_view(), name="profile-update"),
]