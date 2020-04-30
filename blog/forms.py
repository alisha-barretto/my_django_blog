from django import forms
from django.db import models
# from django.contrib.comments.models import Comment
# from django_comments.models import Comment
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
         model = Comment
         fields = ('author','text',)