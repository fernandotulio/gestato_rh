from django.urls import path
from .views import (
    ConsultasList,
    ConsultaEdit,
    #FuncionarioDelete,
    ConsultaNovo,
)


urlpatterns = [
    path('', ConsultasList.as_view(), name='list_consultas'),
    path('novo/<int:animal_id> <int:cliente_id>/', ConsultaNovo.as_view(), name='create_consulta'),
    path('editar/<int:pk>/', ConsultaEdit.as_view(), name='update_consulta'),

]