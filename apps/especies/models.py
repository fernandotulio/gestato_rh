from django.db import models
from django.urls import reverse


class Especie(models.Model):
    nome = models.CharField(max_length=70)

    def get_absolute_url(self):
        return reverse('list_especies')


    def __str__(self):
        return self.nome