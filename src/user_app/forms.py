from django import forms
from . import models



class CustomerCreateForm(forms.ModelForm):
    email = forms.CharField(
        required=True,
        label='Электронная почта',)
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='Имя')
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label='Фамилия')
    phone = forms.CharField(
        max_length=15,
        label='Телефон')
    address = forms.CharField(
        required=True,
        label='Адрес доставки')
    additional_info = forms.CharField(
        label='Дополнительная информация',
        widget=forms.Textarea)

    class Meta:
        model = models.Customer
        fields = ['email', 'first_name', 'last_name', 'phone',
              'address', 'additional_info', ]
        
