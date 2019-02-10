from django.views.generic import (
    #ListView,
    UpdateView,
    #DeleteView,
    CreateView
)

from .models import Contato


class ContatoEdit(UpdateView):
    model = Contato
    fields = ['contato', 'tipo_contato',  'observacao']


class ContatoNovo(CreateView):
        model = Contato
        fields = ['contato', 'tipo_contato', 'observacao']

        def post(self, request, *args, **kwargs):
            form = self.get_form()
            form.instance.pertence_id = self.kwargs['cliente_id']

            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
