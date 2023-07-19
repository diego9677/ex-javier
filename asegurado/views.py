from django.urls import reverse_lazy
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Asegurado, Persona
from .forms import AseguradoForm

# Create your views here.


def asegurado_list(request: HttpRequest):
    asegurados = Asegurado.objects.all()
    return render(request, 'asegurado/asegurado_list.html', {'asegurados': asegurados})


def crear_asegurado(request: HttpRequest):
    if request.method == 'POST':
        form = AseguradoForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            persona = Persona.objects.create(
                nombres=form.cleaned_data['nombres'],
                apellidos=form.cleaned_data['apellidos'],
                documento_ideentidad=form.cleaned_data['ci']
            )
            Asegurado.objects.create(
                persona=persona,
                foto=form.cleaned_data['foto'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                certificado_nacimiento=form.cleaned_data['certificado_nacimiento'],
                documento_identidad=form.cleaned_data['documento_identidad'],
                parent=form.cleaned_data['parent'],
                contratos=form.cleaned_data['contratos']
            )
            return redirect(reverse_lazy('asegurado-list'))
        return render(request, 'asegurado/asegurado_form.html', {'form': form})
    context = {'form': AseguradoForm()}
    return render(request, 'asegurado/asegurado_form.html', context)


def actualizar_asegurado(request: HttpRequest, pk: int):
    asegurado = Asegurado.objects.filter(pk=pk).first()

    if request.method == 'POST':
        request.FILES['foto'] = request.FILES.get('foto', asegurado.foto)
        request.FILES['certificado_nacimiento'] = request.FILES.get(
            'certificado_nacimiento', asegurado.certificado_nacimiento)
        request.FILES['documento_identidad'] = request.FILES.get(
            'documento_identidad', asegurado.documento_identidad)
        form = AseguradoForm(request.POST, request.FILES)
        if form.is_valid():
            asegurado.persona.nombres = form.cleaned_data['nombres']
            asegurado.persona.apellidos = form.cleaned_data['apellidos']
            asegurado.persona.documento_ideentidad = form.cleaned_data['ci']

            asegurado.persona.save()

            asegurado.foto = form.cleaned_data['foto']
            asegurado.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            asegurado.certificado_nacimiento = form.cleaned_data['certificado_nacimiento']
            asegurado.documento_identidad = form.cleaned_data['documento_identidad']
            asegurado.parent = form.cleaned_data['parent']
            # asegurado.contratos.set(form.cleaned_data['contratos'])
            asegurado.save()
            return redirect(reverse_lazy('asegurado-list'))
        return render(request, 'asegurado/asegurado_form.html', {'form': form, 'asegurado': asegurado})

    context = {
        'form': AseguradoForm(
            initial={
                'nombres': asegurado.persona.nombres,
                'apellidos': asegurado.persona.apellidos,
                'ci': asegurado.persona.documento_ideentidad,
                'fecha_nacimiento': asegurado.fecha_nacimiento,
                'foto': asegurado.foto,
                'certificado_nacimiento': asegurado.certificado_nacimiento,
                'documento_identidad': asegurado.documento_identidad,
                'parent': asegurado.parent,
            },
        ),
        'asegurado': asegurado,
    }
    return render(request, 'asegurado/asegurado_form.html', context)


def eliminar_asegurado(request: HttpRequest, pk: int):
    asegurado = Asegurado.objects.filter(pk=pk).first()
    if request.method == 'POST':
        asegurado.delete()
        return redirect(reverse_lazy('asegurado-list'))
    context = {
        'object': asegurado
    }
    return render(request, 'asegurado/asegurado_confirm_delete.html', context)
