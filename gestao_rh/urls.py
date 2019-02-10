from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('documento/', include('apps.documentos.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),
    path('especies/', include('apps.especies.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('enderecos/', include('apps.enderecos.urls')),
    path('contatos/', include('apps.contatos.urls')),
    path('animais/', include('apps.animal.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)