from django.shortcuts import render, redirect, HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def show(request):
    return render(request, 'main_app/index.html')


def post_list(request):
    posts = Post.objects.filter().order_by('-date')
    form = PostForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = PostForm(request.POST)
            if form.is_valid():
                print('DA')
                # post = form.save(commit=False)
                post = form.save()
                post.publish()
                return redirect('home')
            else:
                return redirect('home')
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'main_app/index.html', {'posts': posts})
            else:
                return HttpResponse('<h1>неправильный пароль. или юзернейм. или твоя жизнь</h1>')
    elif request.method == 'GET':
        return render(request, 'main_app/index.html', {'posts': posts})


def log_out(request):
    logout(request)
    print('logged out')
    return render(request, 'main_app.index.html')
