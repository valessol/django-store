from django import forms

class ContactForm(forms.Form):
    nombre_de_contacto = forms.CharField(max_length=30)
    consulta = forms.CharField(max_length=255)
    telefono = forms.IntegerField()
    
