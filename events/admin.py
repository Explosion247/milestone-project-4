from django.contrib import admin
from .models import Event, Comment

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'status']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Comment)