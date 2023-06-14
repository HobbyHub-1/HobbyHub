from django import forms
from .models import Post, PostImage, PostComment, Group, GroupImage, GroupComment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class SomeForm(forms.Form):
    content = forms.CharField(widget=SummernoteWidget()) 

class PostForm(forms.ModelForm):
    title = forms.CharField(label='',
        widget = forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': '제목을 입력하세요',
               'autofocus': True,}),)
    subtitle = forms.CharField(label='',
        widget = forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': '소제목을 입력하세요',}),)
    category = forms.ChoiceField(label='', 
        choices=Group.category_choices, 
        widget=forms.Select(attrs={'class': 'form-select'}),)
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['tags'].label = ''
        self.fields['tags'].widget.attrs.update({
            'placeholder': '태그를 입력해주세요.',
            'class': 'form-control',}),
    class Meta:
        model = Post
        fields = ( 'title','subtitle', 'category', 'content',  'tags',)
        widgets = {
            'content': SummernoteWidget(),
        }
        labels =None

class PostImageFrom(forms.ModelForm):
    image = forms.ImageField(
        label='대표이미지는 3장까지 업로드', 
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
    content = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': '댓글을 입력하세요', }))
    class Meta:
        model = PostComment
        fields = ( 'content',)


class GroupForm(forms.ModelForm):
    title = forms.CharField(label='',
        widget = forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': '제목을 입력하세요',
                'autofocus': True,}),)
    subtitle = forms.CharField(label='',
        widget = forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': '소제목을 입력하세요',}),)
    category = forms.ChoiceField(label='카테고리', 
        choices=Group.category_choices, 
        widget=forms.Select(attrs={'class': 'form-select'}),)
    gender = forms.ChoiceField(label='', 
        choices=Group.gender_choices, 
        widget=forms.Select(attrs={'class': 'form-select'}),)
    propensity = forms.ChoiceField(label='',
        choices=Group.propensity_choices, 
        widget=forms.Select(attrs={'class': 'form-select'}),)
    day = forms.ChoiceField(label='요일', 
        choices=Group.day_choices, 
        widget=forms.Select(attrs={'class': 'form-select', }),)
    region = forms.ChoiceField(label='', 
        choices=Group.region_choices, 
        widget=forms.Select(attrs={'class': 'form-select'}),)
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': '주소를 입력하세요',}))
    
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['tags'].label = ''
        self.fields['tags'].widget.attrs.update({
            'placeholder': '태그를 입력하세요. ',
            'class': 'form-control',})
    class Meta:
        model = Group
        fields = ('title', 'subtitle','category', 'day','gender', 'propensity',  'region', 'address', 'content','tags',)
        widgets = {
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '500px'}}),
        }


class GroupImageFrom(forms.ModelForm):
    image = forms.ImageField(label='', widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True,},), required=False,)

    class Meta:
        model = GroupImage
        fields = ('image',)        


class GroupCommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': '댓글을 입력하세요', }))
    class Meta:
        model = GroupComment
        fields = ( 'content',)
        
