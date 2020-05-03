from django.db import models
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# from django.contrib.comments.models import Comment
# from django_comments.models import Comment
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
         model = Comment
         fields = ('author','text',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Sign up','Sign up', css_class = 'btn-primary'))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']



