from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from blog.models import BlogEntry
from blog.forms import CreateEntryForm, EditEntryForm
from users.models import UserData

class EntriesList(ListView):
    model = BlogEntry
    context_object_name = 'entries_list'
    template_name = 'blog/index.html'
    
    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search:
            entries_list = self.model.objects.filter(title__icontains=search)
        else:
            entries_list = self.model.objects.all()
        return entries_list
    
@login_required
def create_entry(request):
    form = CreateEntryForm()
    if request.method == 'POST':
        form = CreateEntryForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            review = cleaned_data.get('description')[:48] + '...'
            description = cleaned_data.get('description')
            title = cleaned_data.get('title')
            image = cleaned_data.get('image')
            category = cleaned_data.get('category')
            userdata = UserData.objects.filter(user__username=request.user)[0]
            entry = BlogEntry(
                title=title, 
                description=description, 
                image=image, 
                review=review, 
                category=category, 
                userdata=userdata
            )
            entry.save()
            
            userdata.entries += 1
            userdata.save()
            return redirect('entries')
    return render(request, 'blog/create_entry.html', {'form': form})

@login_required
def edit_entry(request, pk):
    logged_user = UserData.objects.filter(user__username=request.user)[0]
    entry = BlogEntry.objects.get(id=pk)
    
    if logged_user == entry.userdata:
        form = EditEntryForm(initial={'title': entry.title, 'description': entry.description, 'image': entry.image})
        
        if request.method == 'POST':
            form = EditEntryForm(request.POST, request.FILES)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                description = cleaned_data.get('description')
                image = cleaned_data.get('image')
                remove_image = request.POST.get('image-clear')
                
                if description:
                    entry.description = description
                    entry.review = description[:48] + '...'
                if image:
                    entry.image = image
                if remove_image:
                    entry.image = ''
 
                entry.title = cleaned_data.get('title')
                entry.save()
                return redirect('entries')
        return render(request, 'blog/edit_entry.html', {'form': form, 'entry_id': pk})
    
def entry_view(request, pk):
    entry = BlogEntry.objects.get(id=pk)
    is_owner = request.user.username == entry.userdata.username
    related_entries = BlogEntry.objects.filter(category=entry.category)

    return render(request, 'blog/entry_view.html', {'entry': entry, 'is_owner': is_owner, 'related_entries': related_entries})
    
class DeleteEntry(LoginRequiredMixin, DeleteView):
    model = BlogEntry
    template_name = 'blog/delete_entry.html'
    success_url = reverse_lazy('')