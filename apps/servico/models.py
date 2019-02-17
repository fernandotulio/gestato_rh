from django.db import models
from apps.animal.models import Animal
from django.urls import reverse



class TiposServico(models.Model):

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_tiposservico')



class Servico(models.Model):

    nome = models.CharField(max_length=100)
    tipo_servico = models.ForeignKey(TiposServico, on_delete=models.PROTECT)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    data  = models.DateField()
    proxima = models.DateField()
    is_anual = models.BooleanField('Anual', default=False)
    observacao = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('update_animal', args=[self.animal.id])
