from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = self.cleaned_data

        return cleaned_data
