from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from users.forms import RegisterForm, EditForm
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
            print('userdata', UserData.objects.all())          
            return redirect('entries')
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
    user_data = request.user.userdata
    form = EditForm(initial={'biography': user_data.biography, 'avatar': user_data.avatar} ,instance=request.user)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            biography = form.cleaned_data.get('biography')
            avatar = form.cleaned_data.get('avatar')
            remove_avatar = request.POST.get('avatar-clear')
            if biography:
                user_data.biography = biography
            if avatar:
                user_data.avatar = avatar
            if remove_avatar:
                user_data.avatar = ''
            user_data.save()
            form.save()
            return redirect('profile_view')
    return render(request, 'users/profile_edit.html', {'form': form})

class ChangePassword(PasswordChangeView):
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('profile_view')