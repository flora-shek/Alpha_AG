from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event,Prayer_request
from .forms import PrayerForm

def index(request):
  events = Event.objects.all().order_by('date')
  template = loader.get_template('layout.html')
  context = {
    'events': events,
  }
  if request.method == "POST":
    form = PrayerForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('')

  return HttpResponse(template.render(context, request))

