from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Comment


class SignupForms(UserCreationForm):
    username = forms.CharField(
        label=None,
        max_length=120,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username',
            }
        )
    )
    email = forms.EmailField(
        label=None,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }
        )
    )
    password1 = forms.CharField(
        label=None,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password',
            }
        )
    )
    password2 = forms.CharField(
        label=None,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your password',
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForms(AuthenticationForm):
    username = forms.CharField(
        label=None,
        max_length=120,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username',
            }
        )
    )
    password = forms.CharField(
        label=None,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password',
            }
        )
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_message', ]
        widgets = {
            'comment_message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your comment',
                    'rows': 5,
                    'id': 'comment'
                }
            )
        }


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=120,
        label=None,
        widget=(
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                    'placeholder': 'Enter your name',
                }
            )
        )
    )
    email = forms.EmailField(
        label=None,
        widget=(
            forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                    'placeholder': 'Enter your email',
                }
            )
        )
    )
    message = forms.CharField(
        label=None,
        max_length=3000,
        widget=(
            forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'message',
                    'placeholder': 'Enter your message',
                    'rows': 5,
                }
            )
        )
    )