#posts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

# Create your views here.
# 1 index
def index(request):
    posts = Post.objects.all()
    context ={
        'posts': posts,
    }
    return render(request,'posts/index.html', context)

# 2 post_detail 내용 조회
def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context ={
        'post': post,
    }
    return render(request,'posts/post_detail.html', context)

# 3 post_create 생성
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

# 4 post_delete 삭제
@login_required
def post_delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        post.delete()
    return redirect('posts:index')

# 5 post_update 수정
@login_required
def post_update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts:post_detail', post_pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('posts:index')
    context ={
        'post': post,
        'form': form,
    }
    return render(request, 'posts/post_update.html', context)
