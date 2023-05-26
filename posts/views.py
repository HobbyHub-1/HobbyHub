#posts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context ={
        'posts': posts,
    }
    return render(request,'posts/index.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context ={
        'post': post,
    }
    return render(request,'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request,'posts/post_create.html', context)


@login_required
def post_delete(request, post_pk):
    post = Article.objects.get(pk=artilce_pk)
    if request.user == article.user:
        article.delete()
    return render(request, 'posts/post_delete.html', context)


@login_required
def post_update(request, post_pk):
    return render(request, 'posts/post_update.html', context)
