from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models, forms

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Вы вошли как {username}.")
                return redirect(reverse_lazy('user:profile-detail'))
            else:
                messages.error(request, "Неправильное имя пользователя или пароль.")
        else:
            messages.error(request, "Неправильное имя пользователя или пароль.")
            messages.error(request, "Пройдите регистрацию или продолжите как не зарегистрированный пользователь.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "user_app/login_entrance.html",
                  context={"form":form})



def logout_view(request):
    logout(request)
    messages.info(request, "Вы вышли из системы.")
    return redirect((reverse_lazy('user:personal-page-list')))




def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse_lazy('user:profile-create'))
    else:
        form = UserCreationForm()
    return render(request, 'user_app/registration.html', {'form': form})



class PersonalPageList(generic.ListView):
    model = models.PersonalPage


class MyLoginView(auth_views.LoginView):
    template_name = "user_app/login.html"
   


class CheckProfileMixin(LoginRequiredMixin):
    redirect_on_missing_profile = True
    def dispatch(self, request, *args, **kwargs):     # отправлять
        if not request.user.is_authenticated:
            return self.handle_no_permission()     
        user = self.request.user
        profile = models.Customer.objects.filter(
            user__pk=user.pk
        )
        redirect_needed = bool(profile)
        if self.redirect_on_missing_profile == True:
            redirect_needed = not redirect_needed
        if redirect_needed:
            return HttpResponseRedirect(self.profile_redirect_url)
        return super().dispatch(request, *args, **kwargs)



class CustomerCreate(CheckProfileMixin, generic.CreateView):
    profile_redirect_url = reverse_lazy('user:profile-detail')
    redirect_on_missing_profile = False
    model = models.Customer
    template_name = "user_app/profile_create.html"
    form_class = forms.CustomerCreateForm
    success_url = reverse_lazy('user:profile-detail')
    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        self.object = profile
        return HttpResponseRedirect(self.get_success_url())




class CustomerUpdate(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('user:login')
    model = models.Customer
    template_name = "user_app/profile_update.html"
    form_class = forms.CustomerCreateForm
    success_url = reverse_lazy('user:profile-detail')
    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        self.object = profile
        return HttpResponseRedirect(self.get_success_url())



class CustomerDetail(CheckProfileMixin, LoginRequiredMixin, generic.DetailView):
    profile_redirect_url = reverse_lazy('user:profile-create')
    login_url = reverse_lazy('user:login')
    redirect_on_missing_profile = True
    template_name = "user_app/profile_detail.html"

    def get_object(self):
        user = self.request.user
        profile = models.Customer.objects.filter(
            user__pk=user.pk
        )
        print(profile)
        if profile:
            profile = profile[0]
        else:
            profile = models.Customer.objects.create(
                user=user,
                email = '',
                first_name = '',
                last_name = '',
                phone = '',
                address='',
                additional_info = '',
                group = '',
            )
        return profile





