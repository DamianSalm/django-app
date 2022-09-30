from email.mime import image
from random import choices
from django.db import models
from datetime import datetime





# create your models here


class foto(models.Model):
    image = models.ImageField(upload_to="img", null=True)

    def __str__(self):
        return str(self.id)

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.TextField(max_length=500)
    aviso = models.BooleanField()
    fecha = datetime.now()

    def __str__(self):
        return self.nombre