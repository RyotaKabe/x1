from django import forms

from .models import Post

#フォーム名がPostForm
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
