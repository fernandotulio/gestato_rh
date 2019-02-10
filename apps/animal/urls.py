from django.urls import path
from .views import (
    AnimalList,
    AnimalEdit,
    AnimalNovo,
    #FuncionarioDelete,
    #ClienteNovo,
)


urlpatterns = [
    path('', AnimalList.as_view(), name='list_animais'),
    #path('novo/', AnimalNovo.as_view(), name='create_animal'),
    path('novo/<int:cliente_id>/', AnimalNovo.as_view(), name='create_animal'),
    path('editar/<int:pk>/', AnimalEdit.as_view(), name='update_animal'),
    #path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),

]
