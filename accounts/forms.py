from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    name = forms.CharField(required = True)
    last = forms.CharField(required = True)
    class Meta:
        model = User
        fields = ('username' , 'email', 'name','last','password1' , 'password2')

    def save(self , commit = True ):
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['last']

        if commit:
            user.save()

        return user


