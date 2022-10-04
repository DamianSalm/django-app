from django.db import models
from datetime import datetime
from django_resized import ResizedImageField




# create your models here


class foto(models.Model):
    nombre = models.CharField(max_length= 150, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Contacto(models.Model):
    list_of_choices = [("0", "Consulta general"), ("1", "Precios"), ("2","Disponibilidad"), ("3","Servicios")]
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    motivo = models.CharField(max_length=1, null=True, choices=list_of_choices)
    mensaje = models.TextField(max_length=255)
    #avisos = models.BooleanField()
    fecha = datetime.now()

    def __str__(self):
        return self.nombre

class Carrousel(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=255)
    entry_date = models.DateTimeField(default=datetime.now)
    imagen = ResizedImageField(size=[450, 450], upload_to="img_carousel", blank=True, null=True)

    def __str__(self):
        return self.titulo