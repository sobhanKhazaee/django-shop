from django import forms


class contactForm(forms.Form):
    full_name = forms.CharField(
        label="نام و نام خانوادگی",
        max_length=50,
        widget=forms.TextInput(att)
                
    )
