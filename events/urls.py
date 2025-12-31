from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name="home"),
    path('<slug:slug>/', views.event_details, name='event_details'),
    path('all_events/', views.all_events, name="all_events")
]