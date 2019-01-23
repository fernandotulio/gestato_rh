from django.views.generic import (
    ListView,
    UpdateView,
    #DeleteView,
    #CreateView
)

from .models import Cliente


class ClientesList(ListView):
    model = Cliente


    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Cliente.objects.filter(empresa=empresa_logada)



class ClienteEdit(UpdateView):
    model = Cliente
    fields = ['nome', 'empresa', 'email', 'telefone','celular','comercial','observacao']

