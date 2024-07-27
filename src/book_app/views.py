from django.shortcuts import render
from django.views import generic as generic_viws
from . import models
# Create your views here.



class ItemCreate(generic_viws.CreateView):
    model = models.Item
    fields = ['title', 'cover']

class ItemDetail(generic_viws.DetailView):
    model = models.Item

 