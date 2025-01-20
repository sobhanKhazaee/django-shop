from django import forms
from account.models import User

class contact_model_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username ', 'email', 'title', 'massage']
        labels = {
            'full_name': "نام و نام خانوادگی",
            'email': "ایمیل",
            'title': "موضوع",
            'massage': "متن پیام"
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'inp_feild',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'email':  forms.EmailInput(attrs={
                'class': "inp_feild",
                'placeholder': "ایمیل خود را وارد کنید"
            }),
            'title':  forms.TextInput(attrs={
                'class': "inp_feild",
                'placeholder': "موضوع پیام را وارد کنید"
            }),
            'massage': forms.Textarea(attrs={
                'class': "text_feild",
                'id': "text_feild",
                'placeholder': "متن پیام را وارد کنید"
            })
        }

        error_messages = {
            'full_name': {
                'required': "لطفا نام خود را وارد کنید",
                'max_length': "این نام خیلی طولانی است"
            },
            'email': {
                'required': "وارد کردن ایمیل الزامی است",
                'max_length': "تعداد کاراکتر های ایمیل بیش از حد مجاز است"
            },
            'title': {
                'required': "وارد کردن موضوع الزامی است",
                'max_length': "تعداد کاراکتر های موضوع بیش از حد مجاز است"
            },
            'massage': {
                'required': "وارد کردن پیام الزامی است",
                'max_length': "پیام شما طولانی است"
            }
        }