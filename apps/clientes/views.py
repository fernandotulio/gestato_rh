from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    UpdateView,
    #DeleteView,
    CreateView
)

from .models import Cliente


#@login_required
class ClientesList(ListView):
    model = Cliente


    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Cliente.objects.filter(empresa=empresa_logada).order_by('nome')


class ClienteEdit(UpdateView):
    model = Cliente
    fields = ['nome', 'empresa', 'is_active', 'cpf', 'rg', 'date_nascimento', 'observacao']



class ClienteNovo(CreateView):
    model = Cliente
    fields = ['nome', 'empresa', 'is_active', 'cpf', 'rg', 'date_nascimento', 'observacao']

    def form_valid(self, form):
        cliente = form.save(commit=False)
        return super(ClienteNovo, self).form_valid(form)





