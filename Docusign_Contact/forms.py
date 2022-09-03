from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter your Full Name ', 'class': 'form-control'}),
        label='Full Name:',
        max_length= 100,
        validators=[
            validators.MaxLengthValidator(150, 'Your full name must be less than 100 characters')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email address ', 'class': 'form-control'}),
        label='Email:',
        max_length=150,
        validators=[
            validators.MaxLengthValidator(100, 'Your Email address must be less than 150 characters')
        ]
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':  'Enter your Phone Number ', 'class': 'form-control'}),
        label='Phone Number',
        max_length=30,
        validators=[
            validators.MaxLengthValidator(200, 'Your subject must be less than 30 characters')
        ]
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':  'Enter your Email address ', 'class': 'form-control'}),
        label='Subject',
        max_length=200,
        validators=[
            validators.MaxLengthValidator(200, 'Your subject must be less than 200 characters')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter your Text ', 'class': 'form-control', 'rows': '8',
                   'cols': '20'}),
        label='Text',
        max_length=1000,
    )