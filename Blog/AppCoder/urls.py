from django.urls import path

from AppCoder.views import inicio
from AppCoder.views import futbolistas_formulario
from AppCoder.views import basquetbolista_formulario
from AppCoder.views import rugbier_formulario
from AppCoder.views import agregar_avatar, RugbiersDeleteView, BasquetbolistasDeleteView, FutbolistasDeleteView, RugbiersUpdateView, BasquetbolistasUpdateView, ContactoListView, FutbolistaListView, RugbiersCreateView, FutbolistasCreateView, FutbolistasUpdateView, BasquetbolistaListView, RugbiersListView, BasquetbolistasCreateView
from AppCoder.views import futbolistas_delete
from AppCoder.views import basquetbolistas_delete
from AppCoder.views import rugbiers_delete
from AppCoder.views import futbolistas_update
from AppCoder.views import basquetbolistas_update
from AppCoder.views import rugbiers_update




urlpatterns = [
    
    path('', inicio, name='inicio'),
    # path('futbolistasFormulario', futbolistas_formulario, name='futbolistas_formulario'),
    # path('basquetbolistasFormulario', basquetbolista_formulario, name='basquetbolistas_formulario'),
    # path('rugbiersFormulario', rugbier_formulario, name='rugbiers_formulario'),
    # path('futbolistas/delete/<id_futbolista>', futbolistas_delete, name='futbolistas_delete'),
    # path('basquetbolistas/delete/<id_basquetbolista>', basquetbolistas_delete, name='basquetbolistas_delete'),
    # path('rugbiers/delete/<id_rugbier>', rugbiers_delete, name='rugbiers_delete'),
    # path('futbolistas/update/<id_futbolista>', futbolistas_update, name='futbolistas_update'),
    # path('basquetbolistas/update/<id_basquetbolista>', basquetbolistas_update, name='basquetbolistas_update'),
    # path('rugbiers/update/<id_rugbier>', rugbiers_update, name='rugbiers_update'),
    path('contacto', ContactoListView.as_view(), name='contacto'),
    path('futbolistas', FutbolistaListView.as_view(), name='futbolistas'),
    path('basquetbolistas', BasquetbolistaListView.as_view(), name='basquetbolistas'),
    path('rugbiers', RugbiersListView.as_view(), name='rugbiers'),
    path('futbolistas/add', FutbolistasCreateView.as_view(), name='futbolistas_form'),
    path('basquetbolistas/add', BasquetbolistasCreateView.as_view(), name='basquetbolistas_form'),
    path('rugbiers/add', RugbiersCreateView.as_view(), name='rugbiers_form'),
    path('futbolistas/update/<pk>', FutbolistasUpdateView.as_view(), name='futbolistas_update'),
    path('basquetbolistas/update/<pk>', BasquetbolistasUpdateView.as_view(), name='basquetbolistas_update'),
    path('rugbiers/update/<pk>', RugbiersUpdateView.as_view(), name='rugbiers_update'),
    path('futbolistas/delete/<pk>', FutbolistasDeleteView.as_view(), name='futbolistas_delete'),
    path('basquetbolistas/delete/<pk>', BasquetbolistasDeleteView.as_view(), name='basquetbolistas_delete'),
    path('rugbiers/delete/<pk>', RugbiersDeleteView.as_view(), name='rugbiers_delete'),
    path('user/avatar/add', agregar_avatar, name='avatar_add'),
    
]