from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Lista_perros


class CreacionUsuarioCustom(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class formularioedita(forms.ModelForm):
    
    class Meta:
        model = Lista_perros
        fields = ['nombre', 'raza_predominante', 'descripcion', 'imagen', 'estado']
    def __init__(self, *args, **kwargs):
        super(formularioedita,self).__init__(*args,**kwargs)
        self.fields['imagen'].required=True
