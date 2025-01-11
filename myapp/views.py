from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Event,Prayer_request
from .forms import PrayerForm
from django.contrib import messages
from django.utils import timezone
def index(request):
    # Fetch all events ordered by date
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    # Handle form submission manually
    if request.method == "POST":
        email = request.POST.get('email')
        prayer_request = request.POST.get('prayerRequest')

        # Check if the required fields are filled
        if email and prayer_request:
            # Create a new PrayerRequest instance and save it
            new_prayer_request = Prayer_request( email=email,request=prayer_request)
            new_prayer_request.save()
            messages.success(request, "Your prayer request has been submitted successfully!")
            return redirect('index')  # Optionally redirect to prevent form resubmission
        else:
            messages.error(request, "Please fill in all fields.")

    # Context for rendering the template
    context = {
        'events': events,
    }

    return render(request, 'layout.html', context)

