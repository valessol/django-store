from django.urls import path
from blog.views import EntriesList, create_entry, EditEntry, EntryView, DeleteEntry

urlpatterns = [
    path('', EntriesList.as_view(), name='entries'),
    path('entry/create', create_entry, name='create_entry'),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry'),
    path('entry/<int:pk>/edit', EditEntry.as_view(), name='edit_entry'),
    path('entry/<int:pk>/delete', DeleteEntry.as_view(), name='delete_entry'),
]