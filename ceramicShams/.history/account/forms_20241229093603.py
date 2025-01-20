from django import forms
from django.core import validators


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'inp_feild'
        }
        ),
      
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild'
        }
        ),
        label="رمز عبور"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild'
        }
        ),
        label="تکرار رمز عبور:"
    )
