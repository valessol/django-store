from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from users.forms import RegisterForm
from users.models import UserData

def login(request):
    form = AuthenticationForm()
    # crear un form que herede del AuthenticationAForm para pisar los labels
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            django_login(request, user)
            UserData.objects.get_or_create(user=request.user)
            return redirect('inicio')
              
    return render(request, 'users/login.html', {'form': form})

def register(request): 
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # aca deberia guardar el user en la otra db
            return redirect('login')
            
    return render(request, 'users/register.html', {'form': form})

def profile_view(request):
    return render(request, 'users/profile_view.html')

def profile_edit(request):
    ...