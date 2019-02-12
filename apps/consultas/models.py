from django.db import models
from apps.clientes.models import Cliente
from apps.animal.models import Animal
from django.urls import reverse

from django import forms

# Create your models here.




class Consulta(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    finalizada = models.BooleanField('Finalizada', default=False)
    sintomas = models.CharField(max_length=2000)
    tratamento = models.CharField(max_length=2000)
    data_consulta = models.DateTimeField(null=True, blank=True)
    data_retorno = models.DateTimeField(null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    observacao = models.CharField(max_length=500, null=True, blank=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)


    def __str__(self):
        return self.animal.nome

    def get_absolute_url(self):
        return reverse('list_consultas')

