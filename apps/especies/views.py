from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Especie


class EspeciesList(ListView):
    model = Especie



class EspecieCreate(CreateView):
    model = Especie
    fields = ['nome']





class EspecieUpdate(UpdateView):
    model = Especie
    fields = ['nome']



class EspecieDelete(DeleteView):
    model = Especie
    success_url = reverse_lazy('list_especies')
