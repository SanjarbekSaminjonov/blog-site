from django.forms import ModelForm, TextInput
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'image',
            'category',
            'region',
        ]
