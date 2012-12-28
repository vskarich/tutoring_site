from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required(login_url='/accounts/login/')
def profile_view(request):
    return render_to_response('accounts/profile.html', {"first_name": request.user.first_name, "last_name": request.user.last_name})
