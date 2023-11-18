from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy

from blog.models import BlogEntry
from comments.models import Comment
from blog.forms import CreateEntryForm, EditEntryForm, AddCommentForm
from users.models import UserData

class EntriesList(ListView):
    model = BlogEntry
    context_object_name = 'entries_list'
    template_name = 'blog/index.html'
    
    def dispatch(self, *args, **kwargs):
        try:
            user = self.request.user
            UserData.objects.get(user=user)
        except:
            logout(self.request)
            
        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search:
            entries_list = self.model.objects.filter(title__icontains=search)
        else:
            entries_list = self.model.objects.all()
        return entries_list
    
    def get_context_data(self):
        context = super().get_context_data()
        categories = []
        entries = self.model.objects.all()
        has_search = False
        if self.request.GET.get('search', ''):
            has_search = True
        for entry in entries:
            categories.append(entry.category)
        context['categories'] = categories
        context['has_search'] = has_search
        return context
    
class CreateEntry(LoginRequiredMixin, FormView):
    template_name = 'blog/create_entry.html'
    form_class = CreateEntryForm
    success_url = '/'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        description = cleaned_data.get('description')
        title = cleaned_data.get('title')
        image = cleaned_data.get('image')
        category = cleaned_data.get('category')
        userdata = UserData.objects.filter(user__username=self.request.user)[0]
        entry = BlogEntry(
            title=title, 
            description=description, 
            image=image, 
            category=category, 
            userdata=userdata
        )
        entry.save()
        
        userdata.entries += 1
        userdata.save()
        return super().form_valid(form)
    
    
# @login_required
# def create_entry(request):
#     form = CreateEntryForm()
#     if request.method == 'POST':
#         form = CreateEntryForm(request.POST, request.FILES)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             description = cleaned_data.get('description')
#             title = cleaned_data.get('title')
#             image = cleaned_data.get('image')
#             category = cleaned_data.get('category')
#             userdata = UserData.objects.filter(user__username=request.user)[0]
#             entry = BlogEntry(
#                 title=title, 
#                 description=description, 
#                 image=image, 
#                 category=category, 
#                 userdata=userdata
#             )
#             entry.save()
            
#             userdata.entries += 1
#             userdata.save()
#             return redirect('entries')
#     return render(request, 'blog/create_entry.html', {'form': form})

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

                if description:
                    entry.description = description
                if image:
                    entry.image = image
                
                entry.title = cleaned_data.get('title')
                entry.save()
                return redirect('entries')
        return render(request, 'blog/edit_entry.html', {'form': form, 'entry_id': pk})
    
def entry_view(request, pk):
    entry = BlogEntry.objects.get(id=pk)
    is_owner = request.user.username == entry.userdata.user.username
    related_entries = BlogEntry.objects.filter(category=entry.category)
    print(entry, related_entries)
    
    form = AddCommentForm()
    
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            comment = cleaned_data.get('comment')
            print(comment)
            blogentry = entry
            userdata = UserData.objects.filter(user__username=request.user)[0]
            new_comment = Comment(blogentry=blogentry, userdata=userdata, comment=comment)
            new_comment.save()
            
            userdata.comments += 1
            userdata.save()
            form = AddCommentForm()
        
    comments = Comment.objects.filter(blogentry=entry)

    return render(request, 'blog/entry_view.html', {'entry': entry, 'is_owner': is_owner, 'related_entries': related_entries, 'comments': comments, 'form': form})

# class EntryView(FormView):
#     template_name = 'blog/entry_view.html'
#     form_class = AddCommentForm

#     def form_valid(self, form):
#         if self.request.method == 'POST':
#             cleaned_data = form.cleaned_data
#             comment = cleaned_data.get('comment')
#             blogentry = self.get_context_data().get('entry')
#             userdata = UserData.objects.filter(user__username=self.request.user)[0]
#             new_comment = Comment(blogentry=blogentry, userdata=userdata, comment=comment)
#             new_comment.save()
            
#             userdata.comments += 1
#             userdata.save()
#         if self.request.method == 'GET':
#             form.fields['comment'] = ''
#         return super().form_valid(form)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         entry = BlogEntry.objects.get(id=self.kwargs.get('pk'))
#         context['entry'] = entry
#         context['is_owner '] = self.request.user.username == entry.userdata.username
#         context['related_entries'] = BlogEntry.objects.filter(category=entry.category)
#         context['comments'] = Comment.objects.all()

#         return context
    
    
class DeleteEntry(LoginRequiredMixin, DeleteView):
    model = BlogEntry
    template_name = 'blog/delete_entry.html'
    success_url = reverse_lazy('entries')
    
    def dispatch(self, *args, **kwargs):
        if self.request.method == 'POST':
            userdata = UserData.objects.filter(user__username=self.request.user)[0]
            
            if userdata.entries:
                userdata.entries -= 1 
            else:
                userdata.entries = 0
            userdata.save()
            
        return super().dispatch(*args, **kwargs)
    

    