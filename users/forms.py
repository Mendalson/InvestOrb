from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm

from . import models


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,
                               label='Пароль')

    password2 = forms.CharField(widget=forms.PasswordInput,
                                label='Подтвердите пароль',
                                help_text='Для подтверждения введите тот же пароль, что и раньше.')

    class Meta:
        model = models.User
        fields = ['username']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Пароли не совпадают")

        password_validation.validate_password(password2, self.instance)
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    username = forms.CharField(widget=forms.TextInput, label='Логин')

    class Meta:
        model = models.User
        fields = ['username', 'password']
