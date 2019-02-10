from django.db import models
from django.urls import reverse
from apps.empresas.models import Empresa


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    is_active = models.BooleanField('Ativo', default=True)
    date_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    rg = models.CharField(max_length=11, null=True, blank=True)
    empresa = models.ManyToManyField(Empresa)
    observacao = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    imagem = models.ImageField( blank=True)

    def get_absolute_url(self):
        return reverse('update_cliente', args=[self.id])

    def __str__(self):
        return self.nome

