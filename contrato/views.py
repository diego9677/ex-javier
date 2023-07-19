from django.http import HttpRequest
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from math import ceil
from .models import Contrato, PlanPago
from .forms import ContratoForm
from datetime import datetime

# Create your views here.


def planes_pago(request: HttpRequest):
    contrato_id = request.GET.get('contrato')
    plan_pago = PlanPago.objects.filter(contrato__id=int(contrato_id)) if contrato_id else None
    context = {
        'contratos': Contrato.objects.all(),
        'contrato_id': contrato_id,
        'plan_pago': plan_pago,
    }

    return render(request, 'contrato/planes_pago.html', context)


def generar_plan_pago(request: HttpRequest, pk: int):
    contrato = Contrato.objects.get(pk=pk)
    current_month = contrato.fecha_inicio.month
    end_month = contrato.fecha_fin.month
    fecha = datetime(contrato.fecha_inicio.year, current_month, 15)
    
    while current_month <= end_month:
        fecha = datetime(fecha.year, current_month, fecha.day)
        PlanPago.objects.create(contrato=contrato, monto=contrato.precio_seguro, fecha_vencimiento=fecha)
        current_month += 1
        
    return redirect(reverse_lazy('plan-pago') + f'?contrato={pk}')


class ContratoListView(ListView):
    model = Contrato
    template_name = 'contrato/contrato_list.html'
    context_object_name = 'contratos'


class ContratoCreateView(CreateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'contrato/contrato_form.html'
    success_url = reverse_lazy('contrato-list')


class ContratoUpdateView(UpdateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'contrato/contrato_form.html'
    success_url = reverse_lazy('contrato-list')


class ContratoDeleteView(DeleteView):
    model = Contrato
    success_url = reverse_lazy('contrato-list')
