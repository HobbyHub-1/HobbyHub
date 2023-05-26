from django import forms
from .models import Post, Post_Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ( 'title', 'content', 'category', 'tags', 'thumbnail',)

class Post_CommentForm(forms.ModelForm):
    class Meta:
        model = Post_Comment
        fields = ( 'content',)
