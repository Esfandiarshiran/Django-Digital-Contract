from django import forms
from django.contrib.auth.models import User
# from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your UserName'}),
        label='User Name:'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": 'Enter your password'}),
        label='Password:'
    )
    # captcha = CaptchaField(
    #     label='Captcha:'
    # )


class UserRegistrationForm(forms.ModelForm):
    # Add extra fild
    # Not that the built-in password doesn't have re_password

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        label='Password'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again'}),
        label='Re-type Password'
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_re_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['re_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['re_password']

    # captcha = CaptchaField()
    # this built in form has all essential features
