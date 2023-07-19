from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Contrato
from .forms import ContratoForm

# Create your views here.


# def contrato_list(request):
#     return render(request, 'contrato/contrato_list.html')


def planes_pago(request):
    return render(request, 'contrato/planes_pago.html')


class ContratoListView(ListView):
    model = Contrato
    template_name = 'contrato/contrato_list.html'


class ContratoCreateView(CreateView):
    model = Contrato


class ContratoUpdateView(UpdateView):
    model = Contrato


class ContratoDeleteView(DeleteView):
    model = Contrato
