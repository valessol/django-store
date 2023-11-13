from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blog.models import BlogEntry

# Class-based views

class EntriesList(ListView):
    model = BlogEntry
    context_object_name = 'entries_list'
    template_name = 'blog/index.html'
    
    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search:
            entries_list = self.model.objects.filter(title__icontains=title)
        else:
            entries_list = self.model.objects.all()
        return entries_list

class CreateEntry(LoginRequiredMixin, CreateView):
    model = BlogEntry
    template_name = 'blog/create_entry.html'
    fields = ['title', 'description', 'image', 'category']
    success_url = reverse_lazy('')
    
class EditEntry(LoginRequiredMixin, UpdateView):
    model = BlogEntry
    template_name = 'blog/edit_entry.html'
    fields = ['title', 'description', 'image', 'category']
    success_url = reverse_lazy('entry/<int:pk>/')
    
class EntryView(DetailView):
    model = BlogEntry
    context_object_name = 'entry'
    template_name = 'blog/entry_view.html'
    
class DeleteEntry(LoginRequiredMixin, DeleteView):
    model = BlogEntry
    template_name = 'blog/delete_entry.html'
    success_url = reverse_lazy('')