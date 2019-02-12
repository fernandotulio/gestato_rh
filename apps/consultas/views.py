from django.views.generic import (
    ListView,
    UpdateView,
    #DeleteView,
    CreateView
)

from .models import Consulta


class ConsultasList(ListView):
    model = Consulta




class ConsultaEdit(UpdateView):
    model = Consulta
    fields = ['cliente', 'animal', 'finalizada', 'sintomas', 'tratamento', 'data_consulta', 'data_retorno', 'peso', 'temperatura', 'observacao']



class ConsultaNovo(CreateView):
    model = Consulta
    fields = ['finalizada', 'sintomas', 'tratamento', 'data_consulta', 'data_retorno', 'peso', 'temperatura', 'observacao']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.animal_id = self.kwargs['animal_id']
        form.instance.cliente_id = self.kwargs['cliente_id']


        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
