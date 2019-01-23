from django.urls import path
from .views import (
    EspeciesList,
    EspecieCreate,
    EspecieUpdate,
    EspecieDelete,
)


urlpatterns = [
    path('list', EspeciesList.as_view(), name='list_especies'),
    path('novo', EspecieCreate.as_view(), name='create_especie'),
    path('update/<int:pk>/', EspecieUpdate.as_view(), name='update_especie'),
    path('delete/<int:pk>/', EspecieDelete.as_view(), name='delete_especie'),

]