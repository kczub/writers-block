from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        qs = Post.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', "This title is taken.")
        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name'
            }),
            'content': forms.Textarea(attrs={
                'cols': 40,
                'rows': 3,
                'placeholder': 'Write a comment...',
            })
        }
        
        labels = {
            'name': False,
            'content': False
        }