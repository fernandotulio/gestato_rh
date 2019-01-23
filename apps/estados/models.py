from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Estado')
    sigla = models.CharField(max_length=2)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('home')


