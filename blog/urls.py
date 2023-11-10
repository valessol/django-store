from django.urls import path
from blog.views import EntriesList, CreateEntry

urlpatterns = [
    path('', EntriesList.as_view(), name='entries'),
    path('entry/create', CreateEntry.as_view(), name='create_entry')
]