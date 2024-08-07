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

class MyLoginView(auth_views.LoginView):
    template_name = "user_app/login.html"


class CustomerCreate(generic.CreateView): #LoginRequiredMixin, 
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

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        profile = models.Customer.objects.filter(
            user__pk=user.pk
        )
        if profile:
            return HttpResponseRedirect(reverse_lazy('user:profile-detail'))
        return super().dispatch(request, *args, **kwargs)

class CustomerDetail(LoginRequiredMixin, generic.DetailView):
    template_name = "user_app/profile_detail.html"

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        profile = models.Customer.objects.filter(
            user__pk=user.pk
        )
        if not profile:
            return HttpResponseRedirect(reverse_lazy('user:profile-create'))
        return super().dispatch(request, *args, **kwargs)

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
                additional_info = 'c-4',
                group = '',
            )
        return profile









# дважды повторяется один код (сверху без повторений)

# class CustomerCreate(LoginRequiredMixin, generic.CreateView):
#     model = models.Customer
#     template_name = "user_app/profile_create.html"
#     form_class = forms.CustomerCreateForm
#     success_url = reverse_lazy('user:profile-detail')
#     def form_valid(self, form):
#         profile = form.save(commit=False)
#         profile.user = self.request.user
#         profile.save()
#         self.object = profile
#         return HttpResponseRedirect(self.get_success_url())

#     def dispatch(self, request, *args, **kwargs):
#         user = self.request.user
#         profile = models.Customer.objects.filter(
#             user__pk=user.pk
#         )
#         if profile:
#             return HttpResponseRedirect(reverse_lazy('user:profile-detail'))
#         return super().dispatch(request, *args, **kwargs)

# class CustomerDetail(LoginRequiredMixin, generic.DetailView):
#     template_name = "user_app/profile_detail.html"

#     def dispatch(self, request, *args, **kwargs):
#         user = self.request.user
#         profile = models.Customer.objects.filter(
#             user__pk=user.pk
#         )
#         if not profile:
#             return HttpResponseRedirect(reverse_lazy('user:profile-create'))
#         return super().dispatch(request, *args, **kwargs)

#     def get_object(self):
#         user = self.request.user
#         profile = models.Customer.objects.filter(
#             user__pk=user.pk
#         )
#         print(profile)
#         if profile:
#             profile = profile[0]
#         else:
#             profile = models.Customer.objects.create(
#                 user=user,
#                 email = '',
#                 first_name = '',
#                 last_name = '',
#                 phone = '',
#                 address='',
#                 additional_info = 'c-4',
#                 group = '',
#             )
#         return profile
















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

