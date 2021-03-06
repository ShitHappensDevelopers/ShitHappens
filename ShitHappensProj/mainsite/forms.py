from django import forms
from . import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 
    


class MyProfileChangeEmailForm(forms.Form):
    new_email = forms.EmailField(help_text="Enter new email", label="Новый эмейл", error_messages={'invalid': 'Такой имейл неподходит'}) 
    new_email.widget.attrs.update({'class':'form-control'})

    def clean_new_email(self):
        newemail = self.cleaned_data['new_email']   
        #check if this email is unique in database
        if User.objects.filter(email__exact=newemail).count() > 0:
            raise ValidationError(_('Такой имейл уже используется другим пользователем'))
        return newemail


class MyProfileChangeUsernameForm(forms.Form):
    new_username = forms.CharField(help_text="Enter new username (login)", label="Новое имя пользователя")
    new_username.widget.attrs.update({'class':'form-control'})

    def clean_new_username(self):
        newusername = self.cleaned_data['new_username']   
        #check if this email is unique in database
        if User.objects.filter(username__exact=newusername).count() > 0:
            raise ValidationError(_('Такое имя пользователя уже используется другим пользователем'))
        return newusername


class MyProfileChangePasswdForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(), help_text="Enter old password", label="Старый пароль")
    new_password1 = forms.CharField(widget=forms.PasswordInput(), help_text="Enter new password", label="Новый пароль")
    new_password2 = forms.CharField(widget=forms.PasswordInput(), help_text="Repeat new password", label="Повторите новый пароль")

    old_password.widget.attrs.update({'class':'form-control'})
    new_password1.widget.attrs.update({'class':'form-control'})
    new_password2.widget.attrs.update({'class':'form-control'})

    def clean_new_password1(self):
        pwd1 = self.cleaned_data['new_password1']   
        #check if this new password is valid 
        if pwd1 == "":
            raise ValidationError(_('Этот пароль не подходит'))
        return pwd1

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get("new_password1")
        pwd2 = cleaned_data.get("new_password2")
        if(pwd1 != pwd2):
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data


class CreateNewStory(forms.Form):
    story_content = forms.CharField(widget=forms.Textarea)
    days_num = forms.IntegerField(widget=forms.NumberInput(), min_value=0, required=False, initial=0)
    hours_num = forms.IntegerField(widget=forms.NumberInput(), min_value=0, max_value=23, required=False, initial=0)
    minutes_num = forms.IntegerField(widget=forms.NumberInput(), min_value=0, max_value=59, required=False, initial=0)

    story_content.widget.attrs.update({'id':'myWriteStoryTxtAr'})
    days_num.widget.attrs.update({'class':'myInputNumber'})
    hours_num.widget.attrs.update({'class':'myInputNumber'})
    minutes_num.widget.attrs.update({'class':'myInputNumber'})


class LoginForm(forms.Form):
    username = forms.CharField(help_text="Enter username or email", label="Логин", widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    passwd = forms.CharField(help_text="Enter password", label="Пароль", widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))


class FiltersForm(forms.Form):
    sort_by = forms.ChoiceField(choices=[('create_date','Дате'), ('like_count','Популярности')], widget=forms.RadioSelect())
    expire_time = forms.IntegerField(widget=forms.NumberInput(), min_value=0, required=False, initial=0)
    last_time = forms.IntegerField(widget=forms.NumberInput(), min_value=0, required=False, initial=0)
    user_login = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'логин'}), required=False, initial="")

    expire_time.widget.attrs.update({'class':'myInputNumber'})
    last_time.widget.attrs.update({'class':'myInputNumber'})


class RegisterNewUserForm(forms.Form):
    username = forms.CharField(help_text="Enter username or email", label="Логин", widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    email = forms.EmailField(help_text="Enter new email", label="Эмейл", error_messages={'invalid': 'Такой имейл неподходит'}, widget=forms.EmailInput(attrs={'placeholder': 'Введите эмейл'}))
    passwd1 = forms.CharField(help_text="Enter password", label="Пароль", widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    passwd2 = forms.CharField(help_text="Enter password", label="Повторите Пароль", widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    def clean_username(self):
        newusername = self.cleaned_data['username']   
        #check if this email is unique in database
        if User.objects.filter(username__exact=newusername).count() > 0:
            raise ValidationError(_('Такое имя пользователя уже используется другим пользователем'))
        return newusername

    def clean_email(self):
        newemail = self.cleaned_data['email']   
        #check if this email is unique in database
        if User.objects.filter(email__exact=newemail).count() > 0:
            raise ValidationError(_('Такой имейл уже используется другим пользователем'))
        return newemail

    def clean_passwd1(self):
        pwd1 = self.cleaned_data['passwd1']   
        #check if this new password is valid 
        if pwd1 == "":
            raise ValidationError(_('Этот пароль не подходит'))
        return pwd1

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get("passwd1")
        pwd2 = cleaned_data.get("passwd2")
        print("test")
        if(pwd1 != pwd2):
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data

