from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from forms import RegistrationForm
from sat_test.models import Test, Score
from django.forms.models import model_to_dict
from django.contrib.auth.models import User





def logout_view(request):
    logout(request)
    return render_to_response('accounts/logout.html', {}, context_instance=RequestContext(request))

def get_score_context(score):
    test = Test.objects.get(id=score.test_id)
    score_context = model_to_dict(score)
    score_context['total_score'] = score.verbal_score + score.math_score + score.analytic_score
    score_context['test'] = model_to_dict(test)
    score_context['test']['date'] = test.get_pretty_date()
    return score_context

@login_required
def account_redirect(request):
    user = request.user
    return HttpResponseRedirect('profile/%s' % user.username)


@login_required
def profile_view(request, username):

    user = User.objects.get(username=username)
    user_context = model_to_dict(user)
    score_context = {}
    scores = Score.objects.filter(student=user)
    score_context['scores'] =  [get_score_context(score) for score in scores]
    context = dict(user_context.items() + score_context.items())

    return render_to_response('accounts/profile.html', context, context_instance=RequestContext(request))

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
                url = urlresolvers.reverse('accounts.views.account_redirect')
                return HttpResponseRedirect(url)
        else:
            return render_to_response('accounts/registration.html', {}, context_instance=RequestContext(request))
    else:
        return render_to_response('accounts/registration.html', {}, context_instance=RequestContext(request))
