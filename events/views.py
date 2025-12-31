from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Event
from .forms import CommentForm


class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('-updated_at')
    template_name = 'events/index.html'
    paginate_by = 3


def event_details(request, slug):
    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    comments = event.comments.all().order_by("-created_at")
    comment_form = CommentForm()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.event = event
            parent_id = comment_form.cleaned_data.get("parent_id")
            if parent_id:
                comment.parent = event.comments.filter(pk=parent_id).first()
            comment.save()
    
    context = {
        'event': event,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(
        request,
        "events/event.html",
        context
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
