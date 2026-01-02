
from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name="home"),
    path('all_events/', views.all_events, name="all_events"),
    path('<slug:slug>/', views.event_details, name='event_details'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.edit_comment, name='edit_comment'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
]
