from django.db import models
from note.models import Note

"""
class Comment(models.Model):
    poster_id = models.IntegerField(default=1)
    post_time = models.DateTimeField('时间', auto_now=True)
    comment = models.CharField('内容', max_length=500)
    note = models.ForeignKey(Note)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.comment

"""



