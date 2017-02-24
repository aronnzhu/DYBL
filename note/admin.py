from django.contrib import admin
from note.models import Note, Comment, Tag
# Register your models here.


@admin.register(Note)

class NoteAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'original_url')
    list_display = ('title', 'poster_id', 'update_time', 'views')
    list_display_links = None
    ordering = ('views',)
    search_fields = ('content',)
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class CommentAdmin(admin.ModelAdmin):
    pass
