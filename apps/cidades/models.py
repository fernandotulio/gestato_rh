from django.db import models
from apps.estados.models import Estado



class Cidade(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da Cidade')
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('home')
