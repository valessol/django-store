from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from comments.models import Comment
from users.models import UserData

class DeleteComment(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comments/delete_comment.html'
    success_url = reverse_lazy('entries')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_id = self.kwargs.get("pk")
        entry= self.model.objects.filter(id=comment_id)[0].blogentry
        context['entry'] = entry
        return context

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'POST':
            userdata = UserData.objects.filter(user__username=self.request.user)[0]
            
            if userdata.comments:
                userdata.comments -= 1 
            else:
                userdata.comments = 0
            userdata.save()
            
        return super().dispatch(*args, **kwargs)