from django.urls import path
from comments.views import DeleteComment

urlpatterns = [
    path('<int:pk>/delete/', DeleteComment.as_view(), name='delete_comment'),
]