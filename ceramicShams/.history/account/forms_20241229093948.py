from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
          label="ایمیل :",
        widget=forms.EmailInput(attrs={
            'class': 'inp_feild'
        }
        ),
      
    )

    password = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild'
        }
        ),
    )
    confirm_password = forms.CharField(
        label="تکرار رمز عبور:",
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild'
        }
        ),
        
    )
    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_pass
