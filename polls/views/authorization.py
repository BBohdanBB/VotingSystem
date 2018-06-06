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
    next=""
    if request.GET:
        next = request.GET['next']
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        args['next'] = next
        if user is not None:
            auth.login(request, user)
            if next == "":
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect(next)
        else:
            args['login_error'] = "User not found"
            return render_to_response('polls/login.html', args)
    else:
        return render_to_response('polls/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            newuser = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/polls')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'polls/reg_form.html', args)
