from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm


def logout_view(request):
    logout(request)
    return render_to_response('accounts/logout.html', {}, context_instance=RequestContext(request))

@login_required
def my_account(request):
    return render_to_response('accounts/profile.html', {"first_name": request.user.first_name, "last_name": request.user.last_name}, context_instance=RequestContext(request))

def signup_view(request):
    return render_to_response('accounts/registration.html', {}, context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = RegistrationForm(postdata)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if new_user and new_user.is_active:
                    login(request, new_user)
                    url = urlresolvers.reverse('accounts.views.my_account')
                    return HttpResponseRedirect(url)
    else:
        return render_to_response('accounts/registration.html', {}, context_instance=RequestContext(request))
