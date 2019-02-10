from django.urls import path
from .views import (
    ClientesList,
    ClienteEdit,
    #FuncionarioDelete,
    ClienteNovo,
)


urlpatterns = [
    path('', ClientesList.as_view(), name='list_clientes'),
    path('novo/', ClienteNovo.as_view(), name='create_cliente'),
    path('editar/<int:pk>/', ClienteEdit.as_view(), name='update_cliente'),
    #path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),

]