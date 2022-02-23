from django import forms
from tinymce.widgets import TinyMCE

from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control'
            }),
            'content': TinyMCE(attrs={
                'cols': 80,
                'rows': 30,
            })
        }
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     qs = Post.objects.filter(title__icontains=title)
    #     if qs.exists():
    #         self.add_error('title', "This title is taken.")
    #     return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'name']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name',
                'class': 'form-control form-control-sm'
            }),
            'content': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Write a comment...',
                'class': 'form-control form-control-sm'
            })
        }
        
        labels = {
            'name': False,
            'content': False
        }