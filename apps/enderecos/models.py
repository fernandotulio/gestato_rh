from django.db import models
from apps.cidades.models import Cidade
from apps.clientes.models import Cliente



class Endereco(models.Model):
    logradouro = models.CharField(max_length=100, help_text='Nome da rua')
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    pertence = models.ForeignKey(Cliente, on_delete=models.PROTECT)


    def __str__(self):
        return self.logradouro

    def get_absolute_url(self):
        return reverse('home')
