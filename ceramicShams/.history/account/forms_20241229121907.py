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
        validators=[validators.MaxLengthValidator(100)]



    )

    password = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild'
        }
        ),
        validators=[validators.MaxLengthValidator(100)]
    )
    confirm_password = forms.CharField(
        label="تکرار رمز عبور:",
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild'
        }),
        validators=[validators.MaxLengthValidator(100)]

    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password == confirm_password:
            return confirm_password

        raise ValidationError(" کلمه عبور با تکرار کلمه عبور تطابق ندارد ")


class LoginForm(forms.Form):

    email = forms.CharField(
        label="ایمیل",
        widget=forms.EmailField(attrs={
            'class': 'inp_feild'
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label="\s,,vn "
    )
