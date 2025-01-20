from django import forms
from .models import contact_us


# class contactForm(forms.Form):
#     full_name = forms.CharField(
#         label="نام و نام خانوادگی",
#         max_length=50,
#         widget=forms.TextInput(attrs={
#             'class': 'inp_feild',
#             'placeholder': 'نام و نام خانوادگی'
#         }),
#         error_messages={
#             'required': "لطفا نام خود را وارد کنید",
#             'max_length': "این نام خیلی طولانی است"
#         }
#     )
#     email = forms.EmailField(
#         label="ایمیل",
#         max_length=50,
#         widget=forms.EmailInput(attrs={
#             'class': "inp_feild",
#             'placeholder': "ایمیل خود را وارد کنید"
#         }),
#         error_messages={
#             'required': "وارد کردن ایمیل الزامی است",
#             'max_length': "تعداد کاراکتر های ایمیل بیش از حد مجاز است"
#         }
#     )
#     title = forms.CharField(
#         label=" موضوع ",
#         max_length=50,
#         widget=forms.TextInput(attrs={
#             'class': "inp_feild",
#             'placeholder': "موضوع پیام را وارد کنید"
#         }),
#         error_messages={
#             'required': "وارد کردن موضوع الزامی است",
#             'max_length': "تعداد کاراکتر های موضوع بیش از حد مجاز است"
#         }
#     )
#     massage = forms.CharField(
#         label=" متن پیام ",
#         max_length=50,
#         widget=forms.Textarea(attrs={
#             'class': "text_feild",
#             'id': "text_feild",
#             'placeholder': "متن پیام را وارد کنید"
#         }),
#         error_messages={
#             'required': "وارد کردن موضوع الزامی است",
#             'max_length': "تعداد کاراکتر های موضوع بیش از حد مجاز است"
#         }
#     )


class contact_model_Form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = ['full_name', 'email', 'title', 'massage']
        labels = {
            'full_name': "نام و نام خانوادگی",
            'email': ,
            'title': "نام و نام خانوادگی",
            'massage': "نام و نام خانوادگی"
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
                'required': "وارد کردن موضوع الزامی است",
                'max_length': "تعداد کاراکتر های موضوع بیش از حد مجاز است"
            }
        }
