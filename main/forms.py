from random import choices
from django import forms
from .models import Contacto



class contact_form(forms.ModelForm):
    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "motivo", "mensaje", "avisos"]
        fields = '__all__'