from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=em
    )