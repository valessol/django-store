from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from blog.models import BlogEntry
from blog.forms import CreateEntryForm
from users.models import UserData
from django.contrib.auth.models import User
# Class-based views

class EntriesList(ListView):
    model = BlogEntry
    context_object_name = 'entries_list'
    template_name = 'blog/index.html'
    
    def get_queryset(self):
        print('------  entries list view  ------')
        search = self.request.GET.get('search', '')
        if search:
            entries_list = self.model.objects.filter(title__icontains=search)
        else:
            entries_list = self.model.objects.all()
        print(entries_list)
        print('------------')
        return entries_list

class CreateEntry(LoginRequiredMixin, CreateView):
    model = BlogEntry
    template_name = 'blog/create_entry.html'
    fields = ['title', 'description', 'image', 'category']
    success_url = reverse_lazy('')
    
@login_required
def create_entry(request):
    form = CreateEntryForm()
    print('-----> user?', request.user)
    if request.method == 'POST':
        form = CreateEntryForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            review = cleaned_data.get('description')[:48] + '...'
            description = cleaned_data.get('description')
            title = cleaned_data.get('title')
            image = cleaned_data.get('image')
            category = cleaned_data.get('category')
            user = UserData.objects.filter(username=request.user)
            print(user.get('user'))
            entry = BlogEntry(
                title=title, 
                description=description, 
                image=image, 
                review=review, 
                category=category, 
                user_id=request.user.userdata.user_id
            )
            entry.save()
            
            user_data = request.user.userdata
            user_data.entries += 1
            user_data.save()
            # entries_list = BlogEntry.objects.all()
            # print(entries_list)
            # return redirect('entries', {'entries_list': entries_list})
            return redirect('entries')
    return render(request, 'blog/create_entry.html', {'form': form})
    
class EditEntry(LoginRequiredMixin, UpdateView):
    model = BlogEntry
    template_name = 'blog/edit_entry.html'
    fields = ['title', 'description', 'image', 'category']
    success_url = reverse_lazy('')
    
class EntryView(DetailView):
    model = BlogEntry
    context_object_name = 'entry'
    template_name = 'blog/entry_view.html'
    
class DeleteEntry(LoginRequiredMixin, DeleteView):
    model = BlogEntry
    template_name = 'blog/delete_entry.html'
    success_url = reverse_lazy('')