from django.db import models
from django.urls import reverse
from apps.empresas.models import Empresa


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ManyToManyField(Empresa)
    email   = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    celular  = models.CharField(max_length=15, null=True, blank=True)
    comercial = models.CharField(max_length=15, null=True, blank=True)
    observacao = models.CharField(max_length=300, null=True, blank=True)


    imagem = models.ImageField( blank=True)

    def get_absolute_url(self):
        return reverse('list_clientes')

    def __str__(self):
        return self.nome

