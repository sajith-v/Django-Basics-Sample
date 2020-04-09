from django import forms
from django.core import validators
import re
from django.contrib.auth.models import User
from first_app.models import UserInfo


def checkName(value):
    if(len(value)<=0):
        raise forms.ValidationError("Name should not be empty")
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(value) != None):
         raise forms.ValidationError("Name should not contains any special character")


class BasicForm(forms.Form):
    name = forms.CharField(validators=[checkName])
    url = forms.URLField()


class UserForm(forms.ModelForm):

    password = forms.CharField(widget= forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email' , 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('ProfilePicture', 'DateOfBirth')
