from django.views.generic import (
    #ListView,
    UpdateView,
    #DeleteView,
    CreateView
)

from .models import Endereco


class EnderecoEdit(UpdateView):
    model = Endereco
    fields = ['tipo_endereco', 'logradouro', 'complemento', 'numero', 'cep', 'bairro', 'cidade', 'observacao']


class EnderecoNovo(CreateView):
        model = Endereco
        fields = ['tipo_endereco', 'logradouro', 'complemento', 'numero', 'cep', 'bairro', 'cidade', 'observacao']

        def post(self, request, *args, **kwargs):
            form = self.get_form()
            form.instance.pertence_id = self.kwargs['cliente_id']

            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

