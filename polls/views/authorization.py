from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from polls.forms import RegistrationForm

def login(request):
    response = "ssss"
    return HttpResponse(response)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/polls')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'polls/reg_form.html', args)