from django import forms
import datetime
from django.core import validators
from django.contrib.auth.models import User

# from captcha.fields import CaptchaField


contract_placeholder_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor' \
                            ' Lorem ipsum dolor sit amet, consecteturLorem ipsum dolor sit amet, consectetur ' \
                            'adipiscing elit,sed do eiusmod tempor Lorem ipsum dolor sit amet,Lorem ipsum dolor ' \
                            'sit amet, consectetur adipiscing elit,sed do eiusmod tempor Lorem ipsum dolor sit amet,' \
                            'Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor Lorem ipsum ' \
                            'dolor sit amet,Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor ' \
                            'Lorem ipsum dolor sit amet,Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do ' \
                            'eiusmod tempor Lorem ipsum dolor sit amet,Lorem ipsum dolor sit amet, consectetur ' \
                            'adipiscing elit,sed do eiusmod tempor Lorem ipsum dolor sit amet,Lorem ipsum ' \
                            'dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor Lorem ' \
                            'ipsum dolor sit amet,Lorem ipsum dolor sit amet, consectetur adipiscing' \
                            ' elit,sed do eiusmod tempor Lorem ipsum dolor sit amet,Lorem ipsum dolor sit ' \
                            'amet, consectetur adipiscing elit,sed do eiusmod tempor Lorem ipsum dolor sit amet.'


class ContractForm(forms.Form):
    contract = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': contract_placeholder_text}),
        label='Contract Text:',
        max_length=100000,
        validators=[
            validators.MaxLengthValidator(100000, 'Your text must be less than 100000 characters')
        ]

    )


class SignForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter recipients Full Name '}),
        label='Full Name:',
        max_length=100,
        validators=[
            validators.MaxLengthValidator(150, 'Your full name must be less than 100 characters')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter recipients Email address '}),
        label='Email:',
        max_length=150,
        validators=[
            validators.MaxLengthValidator(100, 'signer Email address must be less than 150 characters')
        ]
    )

    date = forms.DateField(
        widget=forms.TextInput(attrs={'placeholder': datetime.date.today()}),
        label='Date:',
    )

