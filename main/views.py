from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
#from django.template.loader import get_template
from .models import foto, Carrousel
from .forms import contact_form


# create your views here


#INDEX
def index(request):
    imgs=foto.objects.all()
    carousel=Carrousel.objects.all()

    ctx={
        'form':contact_form(),
        'obj':carousel
    }

    if request.method == 'POST':
        formulario = contact_form(data=request.POST)
        if formulario.is_valid:
            lista_de_motivos = {0: "Consulta general", 1: "Precios", 2: "Disponibilidad", 3: "Servicios"}
            ctx['mensaje'] = "Gracias por ponerte en contacto."
            subject, from_email, to = "Nuevo contacto desde WEB Alquiler", request.POST['correo'], 'german.salmi@gmail.com'
            text_alt = "Mensaje desde la web: Nombre: "+request.POST['nombre']+'. Motivo de la consulta: '+lista_de_motivos[int(request.POST['motivo'])]+'. Correo: '+request.POST['correo']+'. Mensaje: '+request.POST['mensaje']+""
            html_message = "<h1>Mensaje desde la web: </h1><p><br> Nombre: "+request.POST['nombre']+'. <br> Motivo de la consulta: '+lista_de_motivos[int(request.POST['motivo'])]+'. <br> Correo: '+request.POST['correo']+'. <br> Mensaje: '+request.POST['mensaje']+"</p>"
            msg = EmailMultiAlternatives(subject, text_alt, from_email, [to])
            msg.attach_alternative(html_message, "text/html")
            msg.send()
            return redirect('index')
        else:
            ctx['mensaje'] = "Error sending the message"
    


    return render(request, "main/index.html", ctx)



#GALLERY
def gallery(request):
    imgs=foto.objects.all()
    ctx={
        'imgs':imgs
    }
    
    return render(request, "main/gallery.html", ctx)



#MAPS
def maps(request):
    
    return render(request, "main/maps.html", {})




#CONTACT
def contacto(request):
    ctx = {
        'form':contact_form()
        }
    if request.method == 'POST':
        formulario = contact_form(data=request.POST)
        if formulario.is_valid:
            lista_de_motivos = {0: "Consulta general", 1: "Precios", 2: "Disponibilidad", 3: "Servicios"}
            ctx['mensaje'] = "Gracias por ponerte en contacto."
            subject, from_email, to = "Nuevo contacto desde WEB Alquiler", request.POST['correo'], 'german.salmi@gmail.com'
            text_alt = "Mensaje desde la web: Nombre: "+request.POST['nombre']+'. Motivo de la consulta: '+lista_de_motivos[int(request.POST['motivo'])]+'. Correo: '+request.POST['correo']+'. Mensaje: '+request.POST['mensaje']+""
            html_message = "<h1>Mensaje desde la web: </h1><p><br> Nombre: "+request.POST['nombre']+'. <br> Motivo de la consulta: '+lista_de_motivos[int(request.POST['motivo'])]+'. <br> Correo: '+request.POST['correo']+'. <br> Mensaje: '+request.POST['mensaje']+"</p>"
            msg = EmailMultiAlternatives(subject, text_alt, from_email, [to])
            msg.attach_alternative(html_message, "text/html")
            msg.send()
            return redirect('index')
        else:
            ctx['mensaje'] = "Error sending the message"


    return render(request, "main/contacto.html", ctx)
