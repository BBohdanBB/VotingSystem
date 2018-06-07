from __future__ import print_function
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from polls.forms import RegistrationForm
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf



def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(request.POST.get('next', '/'))
            return redirect(request.POST.get('next', '/'))
        else:
            args['login_error'] = "User not found"
            return render_to_response('polls/login.html', args)

    else:
        return render_to_response('polls/login.html', args)

def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    if request.POST:
        newuser_form = RegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('polls/reg_form.html', args)




