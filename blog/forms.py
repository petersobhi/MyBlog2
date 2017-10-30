from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class PostForm(forms.ModelForm):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','id':'subject'}))

    body = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','id':'body'}))

    class Meta:
        model = Post
        fields = ('subject', 'body',)
