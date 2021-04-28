from django import forms
from django.core import validators

from base_user_account.models import User


class LoginForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'شماره تلفن خود را وارد کنید.', 'class': 'form-control input-border'}),
        validators=[
            validators.MaxLengthValidator(limit_value=11, message='مقدار شماره نمی تواند بیشتر از 11 رقم باشد'),
            validators.MinLengthValidator(limit_value=10, message='مقدار شماره نمی تواند کمتر از 10 رقم باشد')
        ]

    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'رمز خود را وارد کنید.', 'class': 'form-control input-border'})
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام', 'class': 'form-control input-border'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام خانوادگی', 'class': 'form-control input-border'})
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'شماره تلفن', 'class': 'form-control input-border'}),
        validators=[
            validators.MaxLengthValidator(limit_value=11, message='مقدار شماره نمی تواند بیشتر از 11 رقم باشد'),
            validators.MinLengthValidator(limit_value=10, message='مقدار شماره نمی تواند کمتر از 10 رقم باشد')
        ]

    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'ایمیل (اختیاری)', 'class': 'form-control input-border'}),
        required=False
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'رمز عبور', 'class': 'form-control input-border'})
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'تکرار رمز عبور', 'class': 'form-control input-border'})
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_exists_user_by_phone = User.objects.filter(phone=phone).exists()
        if is_exists_user_by_phone:
            raise forms.ValidationError("کاربری با این شماره قبلا ثبت نام کرده است")
        return phone

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه های عبور یکسان نیستند!')
        return re_password
