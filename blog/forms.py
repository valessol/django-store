from django import forms
from ckeditor.fields import RichTextFormField

from blog.models import BlogEntry
from comments.models import Comment

class CreateEntryForm(forms.Form):
    title = forms.CharField(label='Título')
    description = RichTextFormField(label='Descripción')
    image = forms.ImageField(label='Imagen')
    category = forms.CharField(label='Categoría')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
    
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
    comment = forms.CharField(max_length=300)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs['class'] = 'form-control'
        self.fields['comment'].widget.attrs['placeholder'] = '¡Únete a la discusión!'
        self.fields['comment'].widget.attrs['rows'] = 3
        self.fields['comment'].widget.attrs['cols'] = 3
    
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {
            'comment': None
        }