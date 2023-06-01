from django import forms
from .models import Post, PostImage, PostComment, Group, GroupImage, GroupComment

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
    day = forms.ChoiceField(label='Day', choices=Group.day_choices, widget=forms.Select(attrs={'class': 'form-select'}),)
    region = forms.ChoiceField(label='Region', choices=Group.region_choices, widget=forms.Select(attrs={'class': 'form-select'}),)
    gender = forms.ChoiceField(label='Gender', choices=Group.gender_choices, widget=forms.Select(attrs={'class': 'form-select'}),)
    Propensity = forms.ChoiceField(label='Propensity', choices=Group.Propensity_choices, widget=forms.Select(attrs={'class': 'form-select'}),)
    category = forms.ChoiceField(label='Category', choices=Group.category_choices, widget=forms.Select(attrs={'class': 'form-select'}),)
    class Meta:
        model = Group
        fields = ('title', 'content', 'tags', 'category',)


class GroupImageFrom(forms.ModelForm):
    image = forms.ImageField(label='모임 소개 이미지 업로드', widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True,},), required=False,)

    class Meta:
        model = GroupImage
        fields = ('image',)        


class GroupCommentForm(forms.ModelForm):
    class Meta:
        model = GroupComment
        fields = ( 'content',)