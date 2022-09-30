from django.shortcuts import render
from .models import foto
from .forms import contact_form

# create your views here
def index(request):
    imgs=foto.objects.all()
    ctx={
        'imgs':imgs,
        'form':contact_form()
    }

    if request.method == 'POST':
        formulario = contact_form(data=request.POST)
        if formulario.is_valid:
            ctx['mensaje'] = "Gracias por ponerte en contacto."
            formulario.save()
        else:
            ctx['mensaje'] = "Error"
    
    
    return render(request, "main/index.html", ctx)


def contacto(request):


    ctx = {
        'form':contact_form()
    }
    if request.method == 'POST':
        formulario = contact_form(data=request.POST)
        if formulario.is_valid:
            ctx['mensaje'] = "Gracias por ponerte en contacto."
            formulario.save()
        else:
            ctx['mensaje'] = "Error"
    return render(request, "main/contacto.html", ctx)


def gallery(request):
    imgs=foto.objects.all()
    ctx={
        'imgs':imgs
    }
    
    return render(request, "main/gallery.html", ctx)


def maps(request):

    
    return render(request, "main/maps.html", {})
