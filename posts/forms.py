from django import forms
from .models import Post, PostImage, PostComment, Group, GroupImage, GroupComment
from taggit.forms import TagField
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    tags = TagField()
    class Meta:
        model = Post
        fields = ( 'title', 'content', 'category', 'tags',)
        widgets = {
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        }


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
    title = forms.CharField(label='',
        widget = forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': '제목을 입력하세요',}),)
    tags = TagField(label='',
        widget=TagField())
    day = forms.ChoiceField(label='', 
        choices=Group.day_choices, 
        widget=forms.Select(attrs={'class': 'form-select', }),)
    region = forms.ChoiceField(label='', 
        choices=Group.region_choices, 
        widget=forms.Select(attrs={'class': 'form-select'}),)
    gender = forms.ChoiceField(label='', 
        choices=Group.gender_choices, 
        widget=forms.Select(attrs={'class': 'form-select'}),)
    propensity = forms.ChoiceField(label='',
        choices=Group.propensity_choices, 
        widget=forms.Select(attrs={'class': 'form-select'}),)
    category = forms.ChoiceField(label='', 
        choices=Group.category_choices, 
        widget=forms.Select(attrs={'class': 'form-select'}),)
    class Meta:
        model = Group
        fields = ('title', 'tags', 'category', 'day', 'region', 'gender', 'propensity', 'content','address',)
        widgets = {
        'content': SummernoteWidget(),}
        labels =None


class GroupImageFrom(forms.ModelForm):
    image = forms.ImageField(label='모임 소개 이미지 업로드', widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True,},), required=False,)

    class Meta:
        model = GroupImage
        fields = ('image',)        


class GroupCommentForm(forms.ModelForm):
    class Meta:
        model = GroupComment
        fields = ( 'content',)
