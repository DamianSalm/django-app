from django import forms
from .models import Contacto



class contact_form(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "mensaje", "avisos"]
        fields = '__all__'
