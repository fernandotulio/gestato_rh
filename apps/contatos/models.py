from django.db import models
from apps.clientes.models import Cliente
from apps.especies.models import Especie
from django.urls import reverse



CELULAR = 'CELULAR'
TELEFONE_RES = 'TELEFONE RESIDENCIAL'
TELEFONE_COMER = 'TELEFONE COMERCIAL'
EMAIL = 'EMAIL'

TIPO_CONTATO = (
    (CELULAR, 'CELULAR'),
    (TELEFONE_RES, 'TELEFONE RESIDENCIAL'),
    (TELEFONE_COMER, 'TELEFONE COMERCIAL'),
    (EMAIL, 'EMAIL'),
)


class Contato(models.Model):
    contato = models.CharField(max_length=100)
    pertence = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tipo_contato = models.CharField(
        max_length=40,
        choices=TIPO_CONTATO,
        default=CELULAR,
    )
    observacao = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.contato

    def get_absolute_url(self):
        return reverse('update_cliente', args=[self.pertence.id])
