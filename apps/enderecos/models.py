from django.db import models
from apps.cidades.models import Cidade
from apps.clientes.models import Cliente
from django.urls import reverse


COMERCIAL = 'COMERCIAL'
RESIDENCIAL = 'RESIDENCIAL'

TIPO_ENDERECO = (
    (COMERCIAL, 'COMERCIAL'),
    (RESIDENCIAL, 'RESIDENCIAL'),
)


class Endereco(models.Model):

    tipo_endereco = models.CharField(
        max_length=40,
        choices=TIPO_ENDERECO,
        default=RESIDENCIAL,
    )
    logradouro = models.CharField(max_length=100, help_text='Nome da rua')
    complemento = models.CharField(max_length=40, null=True, blank=True)
    numero = models.CharField(max_length=8, null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)
    bairro = models.CharField(max_length=40, null=True, blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    observacao = models.CharField(max_length=300, null=True, blank=True)

    pertence = models.ForeignKey(Cliente, on_delete=models.PROTECT)


    def __str__(self):
        return self.logradouro

    def get_absolute_url(self):
        return reverse('update_cliente', args=[self.pertence.id])
