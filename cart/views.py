from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from django.contrib import messages

import stripe
# Create your views here.


def Cart(request, ticket_id=None):
    """Create a Stripe checkout session or render the cart page."""
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == "POST":
        event_id = request.POST.get("event_id")
        event_slug = request.POST.get("event_slug")
        # Allow the user to pick a ticket quantity; fallback to 1 if invalid.
        try:
            quantity = int(request.POST.get("quantity", "1"))
        except (TypeError, ValueError):
            quantity = 1
        if quantity < 1:
            quantity = 1

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": "price_1SlShSIPmHf4wsyQpJoPRjzl",
                    "quantity": quantity,
                }
            ],
            mode="payment",
            success_url=request.build_absolute_uri(
                reverse("success")
                + (f"?event_slug={event_slug}" if event_slug else "")
            ),
            cancel_url=request.build_absolute_uri(
                reverse("cancel")
                + (f"?event_slug={event_slug}" if event_slug else "")
            ),
            # Pass through identifiers so you can reconcile in webhooks later.
            metadata={
                "event_id": event_id,
                "event_slug": event_slug,
                "ticket_id": ticket_id,
                "quantity": quantity,
            },
        )
        return redirect(checkout_session.url, code=303)
    return render(request, "cart/cart.html")


def success(request):
    """
    On successful checkout, send the user back to the event details page
    when possible; otherwise show a simple success page.
    """
    event_slug = request.GET.get("event_slug")
    if event_slug:
        messages.success(request, "Payment successful! Thanks for your purchase.")
        return redirect(reverse("event_details", args=[event_slug]))
    return render(request, "cart/success.html")


def cancel(request):
    """
    On canceled checkout, send the user back to the event details page
    when possible; otherwise show a simple success page.
    """
    event_slug = request.GET.get("event_slug")
    if event_slug:
        messages.warning(request, "Payment canceled.")
        return redirect(reverse("event_details", args=[event_slug]))
    return render(request, "cart/cancel.html")
