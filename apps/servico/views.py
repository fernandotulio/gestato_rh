from django.views.generic import (
    ListView,
    UpdateView,
    #DeleteView,
    CreateView
)

from .models import TiposServico
from .models import Servico


class TiposServicoList(ListView):
    model = TiposServico
    def get_queryset(self):
         return TiposServico.objects.order_by('nome')


class TiposServicoEdit(UpdateView):
    model = TiposServico
    fields = ['nome']


class TiposServicoNovo(CreateView):
    model = TiposServico
    fields = ['nome']

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)




class ServicoList(ListView):
    model = Servico
    def get_queryset(self):
         return Servico.objects.order_by('nome')



class ServicoEdit(UpdateView):
    model = Servico
    fields = ['nome', 'tipo_servico', 'data', 'proxima', 'is_anual', 'observacao']



class ServicoNovo(CreateView):
    model = Servico
    fields = ['nome', 'tipo_servico', 'data', 'proxima', 'is_anual', 'observacao']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.animal_id = self.kwargs['animal_id']



        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)