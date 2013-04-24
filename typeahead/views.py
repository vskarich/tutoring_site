from django.contrib.auth.models import User
import json
from django.shortcuts import HttpResponse


def prefetch(request):
    users = User.objects.all()
    datums = [create_datum(user) for user in users]
    prefetch_data = json.dumps(datums)
    return HttpResponse(prefetch_data, content_type="application/json")

def create_datum(user):
    datum = {}
    datum['tokens'] = get_tokens(user.first_name, user.last_name)
    datum['url'] = '/profile/' + user.username
    datum['username'] = user.username
    datum['value'] = user.first_name + ' ' + user.last_name
    return datum

def get_tokens(first_name, last_name):
    return [first_name.lower(), last_name.lower()]