from django.urls import path
from .views import asegurado_list, crear_asegurado, actualizar_asegurado, eliminar_asegurado

urlpatterns = [
    path('list/', asegurado_list, name='asegurado-list'),
    path('create/', crear_asegurado, name='asegurado-create'),
    path('update/<int:pk>/',
         actualizar_asegurado, name='asegurado-update'),
    path('delete/<int:pk>/',
         eliminar_asegurado, name='asegurado-delete'),
]
