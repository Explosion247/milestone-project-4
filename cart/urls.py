from django.urls import path
from . import views

urlpatterns = [
    # Landing page for cart; used by nav {% url 'cart' %}
    path("", views.Cart, name="cart"),
    path("checkout/<int:ticket_id>/", 
         views.Cart, name="create_checkout_session"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel")  
]
