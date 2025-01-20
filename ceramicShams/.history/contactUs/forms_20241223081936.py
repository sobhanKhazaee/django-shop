from django import forms


class contactForm(forms.Form):
    full_name = forms.CharField(
        label="نام و نام خانوادگی",
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'inp_feild',
            'placeholder': 'نام و نام خانوادگی'
        }),
        error_messages={
            'required': "لطفا نام خود را وارد کنید",
            'max_length': "این نام خیلی طولانی است"
        }
    )
    email = forms.EmailField(
        label="ایمیل",
        max_length=50,
        widget=forms.EmailInput(attrs={
            'class': "inp_feild",
            'placeholder': "ایمیل خود را وارد کنید"
        }),
        error_messages={
            'required': "وارد کردن ایمیل الزامی است",
            'max_length': "تعداد کاراکتر های ایمیل بیش از حد مجاز است"
        }
    )
    title = forms.CharField(
        label="ایمیل",
        max_length=50,
        widget=forms.EmailInput(attrs={
            'class': "inp_feild",
            'placeholder': "ایمیل خود را وارد کنید"
        }),
        error_messages={
            'required': "وارد کردن ایمیل الزامی است",
            'max_length': "تعداد کاراکتر های ایمیل بیش از حد مجاز است"
        }
    )
