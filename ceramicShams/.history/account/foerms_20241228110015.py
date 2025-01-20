from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput,
        label="ایمیل :"
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
    )
    confirmpassword = forms.CharField(
        widget=forms.PasswordInput,
    )
