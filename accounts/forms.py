# accounts/forms.py
from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.exceptions import ValidationError

# 로그인
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label = '아이디',
        widget = forms.TextInput(
            attrs = {}
        )
    )

    password = forms.CharField(
        label = '비밀번호',
        widget = forms.PasswordInput(
            attrs = {}
        )
    )

# 회원가입
class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(label='이름*', widget=forms.TextInput(attrs={'placeholder': '성함을 입력해 주세요'}))
    email = forms.EmailField(
        label='이메일',
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': '이메일을 입력해 주세요'})
        )
    password1 = forms.CharField(
        label='비밀번호*', 
        widget=forms.PasswordInput(attrs={'placeholder' : '영문과 숫자를 조합해주세요'}),
        help_text=None,
        )
    password2 = forms.CharField(
        label='비밀번호 확인*', 
        widget=forms.PasswordInput(attrs={'placeholder' : '비밀번호를 확인해주세요'}),
        )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'name', 'email')
        labels = {
            'username': '아이디*',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder' : '아이디를 입력해주세요'}),
        }
        help_texts = {
            'username': None,
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and get_user_model().objects.filter(username=username).exists():
            raise ValidationError('중복된 아이디입니다.')
        return username

# 회원정보 변경
class CustomUserChangeForm(UserChangeForm):
    password = None
    name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이름'
            }
        )
    )
    
    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일',
            }
        )
    )

    profile_image = forms.ImageField(
        required=False,
        label='프로필 이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'placeholder': '프로필 이미지'
            }
        )
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'name', 'profile_image')


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='현재 비밀번호*', 
        widget=forms.PasswordInput(attrs={})
        )
    new_password1 = forms.CharField(
        label='새로운 비밀번호*', 
        widget=forms.PasswordInput(attrs={})
        )
    new_password2 = forms.CharField(
        label='새로운 비밀번호 확인*', 
        widget=forms.PasswordInput(attrs={})
        )
    
    class Meta:
        model = get_user_model()
        fields = '__all__'