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
from uploads.models import Document
from uploads.forms import DocumentForm


form_fields_to_html_names = {
    'email': 'Email',
    'password1': 'Password',
    'password2': 'Password (Confirm)',
    'first_name': 'First Name',
    'last_name': 'Last Name',
    'username': 'Username'
}


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

    documents = prettify_doc_names(Document.objects.all())
    context['documents'] = documents
    return render_to_response('accounts/profile.html', context, context_instance=RequestContext(request))

def signup_view(request):
    context = {'errors':{}}
    context['names_dict'] = form_fields_to_html_names
    return render_to_response('accounts/registration.html', context, context_instance=RequestContext(request))

def prettify_doc_names(docs):
    for doc in docs:
        old_name = doc.docfile.name
        doc.docfile.name = old_name.split('/')[1]
    return docs

def register(request):
    context = {'errors':{}}
    context['names_dict'] = form_fields_to_html_names
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
            context['errors'] = {name:value for (name, value) in form._errors.items()}
            context['cleaned_data'] = form.cleaned_data
            for key, value in context['cleaned_data'].items():
                if key in context['errors']:
                    del context['cleaned_data'][key]

            return render_to_response('accounts/registration.html', context, context_instance=RequestContext(request))
    else:
        return render_to_response('accounts/registration.html', context, context_instance=RequestContext(request))
