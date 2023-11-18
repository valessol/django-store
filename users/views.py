from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from users.forms import RegisterForm, EditForm, LoginForm
from users.models import UserData
from blog.models import BlogEntry

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            django_login(request, user)
            UserData.objects.get_or_create(user=request.user)     
            return redirect('entries')
    return render(request, 'users/login.html', {'form': form})

def register(request): 
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    return render(request, 'users/register.html', {'form': form})

def profile_view(request):
    userdata = UserData.objects.filter(user=request.user)
    entries = BlogEntry.objects.filter(userdata=userdata[0])
    return render(request, 'users/profile_view.html', {'entries': entries})

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
    
class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = UserData
    template_name = 'users/profile_delete.html'
    success_url = reverse_lazy('entries')
    
    def delete(self, request, *args, **kwargs):
        user = User.objects.filter(id=self.kwargs.get('pk'))
        logout(request)
        user.delete()
        
        return super().delete()

