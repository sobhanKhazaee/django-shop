from django import forms
from account.models import User


class profile_model_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image_profile','username', 'first_name', 'last_name',
                  'email', 'phone_nember', 'address', 'postal_code']
        labels = {
            'image_profile': "عکس پروفایل",
            'username': "نام کاربری",
            'email': "ایمیل",
            'first_name': "نام ",
            'last_name': " نام خانوادگی",
            'phone_nember': "شماره تلفن",
            'address': "آدرس",
            'postal_code': "کد پستی",
        }
        widgets = {
            'image_profile': forms.FileInput(attrs={
                
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
            }),
            'phone_nember': forms.TextInput(attrs={
                'class': "inp_feild",
            }),
            'address': forms.Textarea(attrs={
                'class': "inp_feild",
            }),
            'postal_code': forms.TextInput(attrs={
                'class': "inp_feild",
            }),
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
            },
            'phone_nember': {
                'required': "شماره تلفن خود را وارد کنید",
            },
            'address': {
                'required': "آدرس خود را وارد کنید",
            },
            'postal_code': {
                'required': "کد پستی خود را وارد کنید",
            }
        }

# فرم تغییر رمز عبور


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label='رمز عبور فعلی',
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild',
            'placeholder': 'رمز عبور فعلی'
        }),
        error_messages={
            'required': 'رمز عبور فعلی خود را وارد کنید'
        }
    )
    new_password = forms.CharField(
        label='رمز عبور جدید',
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild',
            'placeholder': 'رمز عبور جدید'
        }),
        error_messages={
            'required': 'رمز عبور جدید خود را وارد کنید'
        }
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور جدید',
        widget=forms.PasswordInput(attrs={
            'class': 'inp_feild',
            'placeholder': 'تکرار رمز عبور جدید'
        }),
        error_messages={
            'required': 'تکرار رمز عبور جدید خود را وارد کنید'
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        if new_password != confirm_password:
            raise forms.ValidationError(
                'رمز عبور جدید و تکرار آن یکسان نیستند')
        return cleaned_data
