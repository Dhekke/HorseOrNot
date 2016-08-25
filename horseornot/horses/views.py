import random

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader

from .models import Horse


def index(request):
    template = loader.get_template('horses/display.html')

    try:
        horse = Horse.objects.order_by('?')[0]
        field = random.choice(['real_profile', 'horse_profile'])
        data = getattr(horse, field)
        context = {
            'horse': horse,
            'content': data,
        }
    except IndexError:
        context = {}

    return render(request, 'horses/display.html', context)

def display_horse(request, profile_id):
    horse = Horse.objects.get(pk=profile_id)
    fields = ['real_profile', 'horse_profile']

    return HttpResponse(getattr(horse, random.choice(fields)))

def submit(request, profile_id):
    if request.POST['profile_pick'] == request.POST['profile']:
        message = 'Correct'
    else:
        message = 'Wrong'

    messages.info(request, message)

    return HttpResponseRedirect(reverse('horses:index'))
