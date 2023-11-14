from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
    
class EditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Email', required=False)
    username = forms.CharField(label='Nombre de usuario', required=False)
    biography= forms.CharField(label='Biografía', max_length=300, required=False, widget=forms.Textarea)
    avatar = forms.ImageField(label='Avatar', required=False)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'biography', 'avatar']