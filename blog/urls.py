from django.urls import path
from blog.views import EntriesList, CreateEntry, EditEntry, EntryView, DeleteEntry

urlpatterns = [
    path('', EntriesList.as_view(), name='entries'),
    path('entry/create', CreateEntry.as_view(), name='create_entry'),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry'),
    path('entry/<int:pk>/edit', EditEntry.as_view(), name='edit_entry'),
    path('entry/<int:pk>/delete', DeleteEntry.as_view(), name='delete_entry'),
]