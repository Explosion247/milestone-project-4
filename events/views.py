from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event


class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1)
    template_name = 'events/index.html'
    paginate_by = 3


def event_details(request, slug):
    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    context = {
        'event': event
    }
    return render(
        request,
        "events/event.html",
        context
    )