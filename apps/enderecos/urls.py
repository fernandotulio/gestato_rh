from django.urls import path
from .views import (
    EnderecoEdit,
    EnderecoNovo,

)


urlpatterns = [
    #path('', AnimalList.as_view(), name='list_animais'),
    #path('novo/', AnimalNovo.as_view(), name='create_animal'),
    path('novo/<int:cliente_id>/', EnderecoNovo.as_view(), name='create_endereco'),
    path('editar/<int:pk>/', EnderecoEdit.as_view(), name='update_endereco'),
    #path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),

]
