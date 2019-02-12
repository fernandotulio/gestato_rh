from django.urls import path
from .views import (
    RacasList,
    RacaEdit,
    #FuncionarioDelete,
    RacaNovo,
)


urlpatterns = [
    path('', RacasList.as_view(), name='list_racas'),
    path('novo/', RacaNovo.as_view(), name='create_raca'),
    path('editar/<int:pk>/', RacaEdit.as_view(), name='update_raca'),

]