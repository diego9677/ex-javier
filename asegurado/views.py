from django.shortcuts import render, redirect, resolve_url
from .models import Asegurado, Persona
from .forms import AseguradoForm

# Create your views here.


def asegurado_list(request):
    asegurados = Asegurado.objects.all()
    return render(request, 'asegurado/asegurado_list.html', {'asegurados': asegurados})


def crear_asegurado(request):
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
                parent=form.cleaned_data['parent']
            )
            return redirect(resolve_url('asegurado-list'))
        return render(request, 'asegurado/asegurado_form.html', {'form': form})
    context = {'form': AseguradoForm()}
    return render(request, 'asegurado/asegurado_form.html', context)


def actualizar_asegurado(request, asegurado_id: int):
    asegurado = Asegurado.objects.filter(pk=asegurado_id).first()

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
            asegurado.save()
            return redirect(resolve_url('asegurado-list'))
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
