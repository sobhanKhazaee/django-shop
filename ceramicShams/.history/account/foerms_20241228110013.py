from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput,
        label="ایمیل :"
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
    )
    copassword = forms.CharField(
        widget=forms.PasswordInput,
    )
