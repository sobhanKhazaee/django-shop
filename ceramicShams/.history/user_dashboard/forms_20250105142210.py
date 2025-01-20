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
            'username': {
                'required': "نام کاربری خود را وارد کنید",
            
            },
            'email': {
                'required': "وارد کردن ایمیل الزامی است",
               
            },
            'first_name': {
                'required': "نام خانوادی ",
              
            },
            'last_name': {
                'required': "وارد کردن الزامی است",
         
            }
        }
