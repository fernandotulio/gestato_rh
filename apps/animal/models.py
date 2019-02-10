from django.db import models
from apps.clientes.models import Cliente
from apps.especies.models import Especie
from django.urls import reverse

from django import forms

# Create your models here.


MACHO = 'M'
FEMEA = 'F'

YEAR_IN_SCHOOL_CHOICES = (
    (MACHO, 'Macho'),
    (FEMEA, 'Femea'),
)


class Animal(models.Model):


    nome = models.CharField(max_length=100)
    pertence = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT)
    sexo = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=MACHO,
    )


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('update_cliente', args=[self.pertence.id])
