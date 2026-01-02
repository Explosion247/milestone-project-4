from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event, Comment, Ticket

# Register your models here.


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'status']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'embeded_map', 'address')


admin.site.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
admin.site.register(Ticket)