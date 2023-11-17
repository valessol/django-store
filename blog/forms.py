from django import forms
from ckeditor.fields import RichTextFormField
from blog.models import BlogEntry
from comments.models import Comment

class CreateEntryForm(forms.Form):
    title = forms.CharField(label='Título')
    description = RichTextFormField(label='Descripción')
    image = forms.ImageField(label='Imagen')
    category = forms.CharField(label='Categoría')
    
    class Meta:
        model = BlogEntry
        fields = ['title', 'description', 'image', 'category']
        
class EditEntryForm(forms.Form):
    title = forms.CharField(label='Título', required=False)
    description = RichTextFormField(label='Descripción', required=False)
    image = forms.ImageField(label='Imagen', required=False)
    
    class Meta:
        model = BlogEntry
        fields = ['title', 'description', 'image']
        
class AddCommentForm(forms.Form):
    comment = forms.CharField(max_length=300, widget=forms.Textarea)
    
    class Meta:
        model = Comment
        fields = ['comment']