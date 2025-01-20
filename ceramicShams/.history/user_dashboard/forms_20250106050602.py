from django import forms
from account.models import User


class profile_model_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': "نام کاربری",
            'email': "ایمیل",
            'first_name': "نام ",
            'last_name': " نام خانوادگی"
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'inp_feild',
                'placeholder': 'نام کاربری'
            }),
            'email':  forms.EmailInput(attrs={
                'class': "inp_feild",
                'placeholder': "ایمیل"
            }),
            'first_name':  forms.TextInput(attrs={
                'class': "inp_feild",

            }),
            'last_name': forms.TextInput(attrs={
                'class': "inp_feild",
            })
        }
        help_texts = {
            'username': '',
        }

        error_messages = {
            'username': {
                'required': "نام کاربری خود را وارد کنید",
            },
            'email': {
                'required': "وارد کردن ایمیل الزامی است",
            },
            'first_name': {
                'required': "نام خود را وارد کنید ",
            },
            'last_name': {
                'required': "نام خانوادگی خود را وارد کنید",
            }
        }

# فرم تغییر رمز عبور
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label='رمز عبور فعلی',
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild',
            'placeholder': 'رمز عبور فعلی'
        })
    )
    new_password = forms.CharField(
        label='رمز عبور جدید',
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild',
            'placeholder': 'رمز عبور جدید'
        })
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور جدید',
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild',
            'placeholder': 'تکرار رمز عبور جدید'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        if new_password != confirm_password:
            raise forms.ValidationError('رمز عبور جدید و تکرار آن یکسان نیستند')
        return cleaned_data