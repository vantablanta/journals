from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Journals


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, label='',widget=forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'email'}))
    username =forms.CharField(max_length=200, label='',widget=forms.TextInput(attrs={'class': 'form-control mb-3','placeholder': 'username'}))
    password1 = forms.CharField(max_length=200,label='',widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'password'}))
    password2 = forms.CharField(max_length=200, label='',widget=forms.PasswordInput(attrs={'class': 'form-control mb-3','placeholder': 'confirm password'}))
    
    class Meta():
       model= User
       fields = ['email', 'username', 'password1', 'password2']

class JournalForm(ModelForm):
    class Meta():
        model = Journals
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'maxlength': '500',}),     
        }

    def __init__(self, *args, **kwargs):
        super(JournalForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ""
