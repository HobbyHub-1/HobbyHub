from django import forms
# from .models import Post, PostImage, PostComment, Group, GroupImage, GroupComment
from .models import Post, PostImage, PostComment, Group, GroupImage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ( 'title', 'content', 'category', 'tags',)


class PostImageFrom(forms.ModelForm):
    image = forms.ImageField(
        label='취미 소개 이미지 업로드', 
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control', 
                'multiple': True,
                },
            ), required=False,
    )

    class Meta:
        model = PostImage
        fields = ('image',)


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ( 'content',)


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'content', 'address', 'category', 'tags',)


class GroupImageFrom(forms.ModelForm):
    image = forms.ImageField(label='모임 소개 이미지 업로드', widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True,},), required=False,)

    class Meta:
        model = GroupImage
        fields = ('image',)        


# class GroupCommentForm(forms.ModelForm):
#     class Meta:
#         model = GroupComment
#         fields = ( 'content',)