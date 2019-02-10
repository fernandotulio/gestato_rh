from django.urls import path
from .views import (
    ContatoEdit,
    ContatoNovo,
)


urlpatterns = [
    path('novo/<int:cliente_id>/', ContatoNovo.as_view(), name='create_contato'),
    path('editar/<int:pk>/', ContatoEdit.as_view(), name='update_contato'),
]
