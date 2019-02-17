from django.db import models
from apps.clientes.models import Cliente
from apps.racas.models import Raca
from django.urls import reverse

from django import forms

# Create your models here.


MACHO = 'M'
FEMEA = 'F'

YEAR_IN_SCHOOL_CHOICES = (
    (MACHO, 'MACHO'),
    (FEMEA, 'FEMEA'),
)


class Animal(models.Model):


    nome = models.CharField(max_length=100)
    pertence = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT)
    sexo = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=MACHO,
    )

    is_active = models.BooleanField('Ativo', default=True)
    #chip = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    date_nascimento = models.DateField(null=True, blank=True)
    idade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    observacao = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('update_cliente', args=[self.pertence.id])
