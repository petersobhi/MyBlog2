from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm, PostForm
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-id')
    form = PostForm()
    return render(request, 'home.html', {'form':form, 'posts': posts})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
