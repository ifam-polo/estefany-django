from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'username': 'username',
            'email': 'email',
            'password': 'password',
        }

        help_texts = {
            'email': 'The e-mail must be valid.'
        }

        error_messages = {
            'username': {
                'required': 'This field must not be empty',
            }
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Type your username here',
                'class': 'input text-input outra-coisa'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here'
            })
        }
