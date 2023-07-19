from django.shortcuts import render

# Create your views here.
def contrato_list(request):
    return render(request, 'contrato/contrato_list.html')


def planes_pago(request):
    return render(request, 'contrato/planes_pago.html')