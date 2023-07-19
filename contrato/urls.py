from django.urls import path
from .views import ContratoCreateView, ContratoUpdateView, ContratoDeleteView, ContratoListView, planes_pago, generar_plan_pago

urlpatterns = [
    path('update/<int:pk>/',
         ContratoUpdateView.as_view(), name='contrato-update'),
    path('delete/<int:pk>/',
         ContratoDeleteView.as_view(), name='contrato-delete'),
    path('list/', ContratoListView.as_view(), name='contrato-list'),
    path('create/', ContratoCreateView.as_view(), name='contrato-create'),
]
