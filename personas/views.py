from django.shortcuts import get_object_or_404, render
from .models import Persona
from .forms import PersonaForm, RawPersonaForm
# Create your views here.

def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        #'nombre': obj.nombres,
        #'edad': obj.edad,
        'objeto': obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView(request):
    obj = Persona.objects.get(id = 2)
    form = PersonaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = PersonaForm()
    
    context = {
        'form': form,
    }
    return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html',{})

def personasAnotherCreateView(request):
    form = RawPersonaForm()
    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'personas/personasCreate.html', context)

def personasShowObject(request, myID):
    obj = Persona.objects.get(id = myID)
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personasDeleteView(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    if request.method == 'POST':
        print("lo borro")
        obj.delete()
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/personasBorrar.html', context)