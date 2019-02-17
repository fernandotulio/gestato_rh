from django.views.generic import (
    ListView,
    UpdateView,
    #DeleteView,
    CreateView
)

from .models import Animal


class AnimalList(ListView):
    model = Animal
    def get_queryset(self):
        return Animal.objects.order_by('nome').all



class AnimalEdit(UpdateView):
    model = Animal
    fields = ['nome', 'raca', 'sexo', 'is_active', 'date_nascimento', 'idade', 'observacao']


class AnimalNovo(CreateView):
        model = Animal
        fields = ['nome', 'raca', 'sexo', 'is_active', 'date_nascimento', 'idade', 'observacao']

        def post(self, request, *args, **kwargs):
            form = self.get_form()
            form.instance.pertence_id = self.kwargs['cliente_id']

            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
