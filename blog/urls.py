from django.urls import path
from django.views.generic.base import TemplateView

from blog.views import EntriesList, CreateEntry, edit_entry, entry_view, DeleteEntry

urlpatterns = [
    path('', EntriesList.as_view(), name='entries'),
    path('entry/create', CreateEntry.as_view(), name='create_entry'),
    path('entry/<int:pk>/', entry_view, name='entry'),
    path('entry/<int:pk>/edit', edit_entry, name='edit_entry'),
    path('entry/<int:pk>/delete', DeleteEntry.as_view(), name='delete_entry'),
    path('about/', TemplateView.as_view(template_name='blog/about.html'), name='about'),
]