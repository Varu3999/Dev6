from django.shortcuts import render , get_object_or_404 , redirect ,render_to_response
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib import auth
from django.template.defaulttags import csrf_token
from django.contrib.auth.forms import UserCreationForm
from .forms import MyRegistrationForm
from .models import Usernotes
from django.contrib import messages
from django.contrib.auth.models import User

def login(request):
    if request.user:
        logout(request)
    return render(request,'accounts/login.html',{})


def auth(request):

    u = request.POST.get('username' , ' ')
    p = request.POST.get('password' , ' ')
    user = authenticate(username=u , password = p)

    if user is not None:
        auth_login(request, user)
        messages.add_message(request,messages.SUCCESS,'Logged in Successfully!!')
        return HttpResponseRedirect('/account/loggedin')
    else:
        messages.add_message(request, messages.SUCCESS, 'Unable to login either User name or password is incorrect!!')
        return HttpResponseRedirect('/account/login')

def loggedin(request):

    un = Usernotes.objects.filter(user =request.user)
    if request.method == 'POST' and request.POST.get("add"):
        notes = request.POST.get('notes','')
        label = request.POST.get('Label','')
        if label == '':
            innote = notes
        else:
            if notes!='':
                a = Usernotes()
                a.user = request.user
                a.notes = notes
                a.subject= label
                a.save()
            innote = ''

    elif request.method == 'POST' and request.POST.get("delete"):
        id = request.POST.get('input')
        innote = ''
        u = Usernotes.objects.filter(id = id)
        u.delete()

    elif request.method == 'POST' and request.POST.get("edit"):
        id = request.POST.get('input')

        us = Usernotes.objects.filter(id = id)
        innote=us[0].notes
        us.delete()
    else:
        innote =''
    # uns = Usernotes.objects.all()
    #
    # if request.method == 'POST':
    #     notes = request.POST.get('notes','')
    #     for un in uns:
    #         if un.user == request.user:
    #             un.notes = un.notes+' '+notes
    #             un.save()
    # t = 0
    # for un in uns:
    #     if un.user == request.user:
    #         notes = un.notes
    #         t = 1
    # if t == 0:
    #     a = Usernotes()
    #     a.user = request.user
    #     a.notes=""
    #     a.save()
    #     notes =""
    # if request.method == 'POST' and request.POST.get("delete"):
    #     print("hi")
    #     for un in uns:
    #         if un.user == request.user:
    #             un.notes =""
    #             un.save()
    return render(request , 'accounts/loggedin.html' , {'fullname':request.user.first_name,'un':un,'innote':innote})

def logout(request):
    auth_logout(request)
    args = {}
    return render(request , 'accounts/logout.html',args)

def invalid(request):
    return render(request , 'accounts/invalid.html')

def register(request):

    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if User.objects.filter(username= request.POST.get('username')).exists():
            messages.add_message(request, messages.ERROR,
                                 'Username already exits!!')
        elif form.is_valid():
            form.save()

            return HttpResponseRedirect('/account/success')
        else:
            messages.add_message(request, messages.ERROR,
                                 '''Please select another password accordin to the guidelines'
                                    Your password can\'t be too similar to your other personal information
                                    Your password must contain at least 8 characters.
                                    Your password can\'t be a commonly used password.
                                    Your password can\'t be entirely numeric.'''
                                 )

    args={}
    args['form']= MyRegistrationForm()
    return render(request,'accounts/register.html', args)

def success(request):
    args = {}
    return render(request,'accounts/success.html',args)

def home(request):
    return render_to_response('accounts/home.html')