from django.views.generic import (
    ListView,
    UpdateView,
    #DeleteView,
    CreateView
)

from .models import Raca


class RacasList(ListView):
    model = Raca


    def get_queryset(self):
        return Raca.objects.order_by('nome')


class RacaEdit(UpdateView):
    model = Raca
    fields = ['nome', 'especie']



class RacaNovo(CreateView):
    model = Raca
    fields = ['nome', 'especie']

    def form_valid(self, form):
        raca = form.save(commit=False)
        return super(RacaNovo, self).form_valid(form)