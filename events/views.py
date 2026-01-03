from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.utils import timezone
from .models import Event, Comment
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
    # ticket_form = TicketForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.name = request.user
            comment.event = event
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been submitted'
            )

        # ticket_form = TicketForm(data=request.POST)
        # if ticket_form.is_valid():
        #     ticket = ticket_form.save(commit=False)
        #     ticket.name = request.user
        #     ticket.event = event
        #     ticket.save()
        #     messages.add_message(
        #         request, messages.SUCCESS,
        #         'ticket purchased'
        #     )

    context = {
        "event": event,
        "comments": comments,
        "comment_form": comment_form,
        # "ticket_form": ticket_form
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


def edit_comment(request, slug, comment_id):

    if request.method == "POST":
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.name == request.user:
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment Updated'
                )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating comment'
            )

        return HttpResponseRedirect(reverse('event_details', args=[slug]))


def delete_comment(request, slug, comment_id):
    comment_form = get_object_or_404(Comment, pk=comment_id)
    if comment_form.name == request.user:
        comment_form.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment deleted'
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own comments'
        )
    return HttpResponseRedirect(reverse('event_details', args=[slug]))