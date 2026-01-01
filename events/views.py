from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Event


class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('-updated_at')
    template_name = 'events/index.html'
    paginate_by = 3


def event_details(request, slug):
    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "events/event.html",
        {"event": event}
    )


def all_events(request):
    now = timezone.now()
    future_events = Event.objects.filter(
        status=1,
        event_date__gte=now
        ).order_by("event_date")
    past_events = Event.objects.filter(
        status=1,
        event_date__lt=now
        ).order_by('-event_date')
    context = {
        "future_events": future_events,
        "past_events": past_events,
    }
    return render(
        request,
        "events/all_events.html",
        context
    )
