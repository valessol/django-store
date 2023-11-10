from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from blog.models import BlogEntry
from django.urls import reverse_lazy

class EntriesList(ListView):
    model = BlogEntry
    context_object_name = 'entries_list'
    template_name = 'blog/index.html'

class CreateEntry(CreateView):
    model = BlogEntry
    template_name = 'blog/create_entry.html'
    fields = ['title', 'description', 'image', 'outstanding', 'category']
    success_url = reverse_lazy('')