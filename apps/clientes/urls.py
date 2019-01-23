from django.urls import path
from .views import (
    ClientesList,
    ClienteEdit,
    #FuncionarioDelete,
    #FuncionarioNovo
)


urlpatterns = [
    path('', ClientesList.as_view(), name='list_clientes'),
    #path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', ClienteEdit.as_view(), name='update_cliente'),
    #path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),

]