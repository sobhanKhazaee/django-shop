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
            'max_length' : "این نام خیلی طط"
        }

    )
