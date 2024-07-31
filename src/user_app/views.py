from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views

# Create your views here.


class MyLoginView(auth_views.LoginView):
    template_name = "user_app/login.html"







# def login_view(request):
#     if request.method == 'GET':
#         return_to = request.GET.get('next')
#         context = {
#             'return_to': return_to
#         }

#         return render(request, 'user_app/login.html', context)
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         redirect_to = request.POST.get('next', '/')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(redirect_to)
#         else:
#             context = {
#                 'error_message': 'Неверный пользователь и/или пароль',
#                 'username': username
#                 }
#             return render(request, 'user_app/login.html', context)

