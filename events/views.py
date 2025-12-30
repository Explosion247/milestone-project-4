from django.shortcuts import render
from django.views import generic
from .models import Event


class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = 'events/index.html'
    paginate_by = 10
