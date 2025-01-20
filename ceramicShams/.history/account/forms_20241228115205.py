from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(att
            ),
        label="ایمیل :"
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        label="رمز عبور"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="تکرار رمز عبور:"
    )
