from django.db import models
from apps.especies.models import Especie
from django.urls import reverse


class Raca(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_racas')

