from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': '.inp_feild'
        }
        ),
        label="ایمیل :"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': '.inp_feild'
        }
        ),
        label="رمز عبور"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="تکرار رمز عبور:"
    )
