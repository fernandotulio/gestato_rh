from django.urls import path
from .views import (
    ServicoList,

    TiposServicoList,
    TiposServicoEdit,
    TiposServicoNovo,
    ServicoEdit,
    ServicoNovo,
    ServicoList

)


urlpatterns = [
    path('tiposservico/', TiposServicoList.as_view(), name='list_tiposservico'),
    path('tiposservico/novo/', TiposServicoNovo.as_view(), name='create_tiposservico'),
    path('tiposservico/editar/<int:pk>/', TiposServicoEdit.as_view(), name='update_tiposservico'),

    path('servico/', ServicoList.as_view(), name='list_servico'),
    path('servico/novo/<int:animal_id>/', ServicoNovo.as_view(), name='create_servico'),
    path('servico/editar/<int:pk>/', ServicoEdit.as_view(), name='update_servico'),

]


