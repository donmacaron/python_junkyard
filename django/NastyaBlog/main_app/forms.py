from django import forms
from .models import Post
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
