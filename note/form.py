from django.forms import ModelForm, Textarea
from note.models import Comment


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        exclude = ('display', 'post_time', 'poster', 'note')

        widgets = {
            'comment': Textarea(attrs={'cols': 110, 'rows': 6})
        }