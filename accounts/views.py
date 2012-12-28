from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return render_to_response('accounts/logout.html', {}, context_instance=RequestContext(request))

@login_required
def my_account(request):
    return render_to_response('accounts/profile.html', {"first_name": request.user.first_name, "last_name": request.user.last_name}, context_instance=RequestContext(request))

def signup_view(request):
    return render_to_response('accounts/registration.html', {}, context_instance=RequestContext(request))

def register(request):
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        postdata = request.POST.copy()
        un = postdata.get('username','')
        pw = postdata.get('password1','')
        new_user = User.objects.create_user(un, postdata.get('email',''), pw)
        new_user.first_name = postdata.get('first_name','')
        new_user.last_name = postdata.get('last_name','')
        new_user.save()
        user = authenticate(username=un, password=pw)
        if user and user.is_active:
                login(request, user)
                url = urlresolvers.reverse('accounts.views.my_account')
                return HttpResponseRedirect(url)
    else:
        return render_to_response('accounts/registration.html', {}, context_instance=RequestContext(request))
