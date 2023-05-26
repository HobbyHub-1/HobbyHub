#posts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Post_Comment
from .forms import PostForm, Post_CommentForm

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
    post_comment_form = Post_CommentForm()
    post_comments = post.post_comment_set.all()
    context ={
        'post': post,
        'post_comment_form': post_comment_form,
        'post_comments': post_comments,
    }
    return render(request,'posts/post_detail.html', context)

# 3 post_create 생성
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
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
            form = PostForm(request.POST, request.FILES, instance=post)
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


def post_comments_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post_comment_form = Post_CommentForm(request.POST)
    if post_comment_form.is_valid():
        post_comment = post_comment_form.save(commit=False)
        post_comment.post = post
        post_comment.user = request.user
        post_comment.save()
        return redirect('posts:post_detail', post_pk)
    context = {
        'post': post,
        'post_comment_form': post_comment_form,
    }
    return render(request, 'posts/post_detail.html', context)


def post_comments_delete(request, post_pk, comment_pk):
    post_comment = Post_Comment.objects.get(pk=comment_pk)
    if request.user == post_comment.user:
        post_comment.delete()
    return redirect('posts:detail', post_pk)


# def post_comments_update(request, post_pk, comment_pk):
#     return render(request, 'posts/post_detail.html', context)


def post_likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
        is_liked = False
    else:
        post.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)
