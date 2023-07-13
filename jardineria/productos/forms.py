from django import forms
from .models import Producto, Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ['nombre', 'tipo', 'precio', 'categoria', 'imagen']
        labels ={
            'nombre':'Nombre',
            'tipo' : 'Tipo',
            'precio': 'Precio',
            'categoria':'Categoria',
            'imagen':'Imagen'
        }
        widgets={

            'nombre':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nombre..',
                    'id': 'nombre',
                    'class': 'form-control',
                }
            ),
            'tipo': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese tipo..',
                    'id':'tipo',
                    'class':'form-control',
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese precio..',
                    'id':'precio',
                    'class':'form-control',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'id':'categoria',
                    'class':'form-control',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id': 'imagen',
                }
            )
        }




class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto 
        fields = ['usuario', 'correo', 'telefono','problema', 'imagen2']
        labels ={
            'usuario':'Usuario',
            'correo' : 'Correo',
            'telefono': 'Telefono',
            'problema': 'Problema',
           
            'imagen2':'Imagen2'
        }
        widgets={

            'usuario':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese usuario..',
                    'id': 'usuario',
                    'class': 'form-control',
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese correo..',
                    'id':'correo',
                    'class':'form-control',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese telefono..',
                    'id':'telefono',
                    'class':'form-control',
                }
            ),
             'problema': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese problema..',
                    'id':'telefono',
                    'class':'form-control',
                }
            ),
           
            'imagen2': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id': 'imagen2',
                }
            )
        }


