from django import forms
from account.models import User


class contact_model_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username ', 'email', 'first_name', 'last_name']
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
            'last_name': forms.Textarea(attrs={
                'class': "inp_feild",
            })
        }

        error_messages = {
            'full_name': {
                'required': "لطفا نام خود را وارد کنید",
            
            },
            'email': {
                'required': "وارد کردن ایمیل الزامی است",
               
            },
            'title': {
                'required': "وارد کردن موضوع الزامی است",
                'max_length': "تعداد کاراکتر های موضوع بیش از حد مجاز است"
            },
            'massage': {
                'required': "وارد کردن پیام الزامی است",
         
            }
        }
