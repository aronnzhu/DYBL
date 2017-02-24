from django.shortcuts import render
from mynote import settings
from comment import models
from note.models import Note, Comment
import logging
from note.form import CommentForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.http import HttpResponseRedirect, StreamingHttpResponse, HttpResponse
# Create your views here.

log = logging.getLogger('django.request')


def get_note(request):
    n = Note.objects.all()
    number = n.count()
    print(type(n))
    paginator = Paginator(n, 2)
    try:
        page = int(request.GET.get('page', 1))
        n = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        n = paginator.page(1)
        pass
    return render(request, 'blog.html', locals())


def read_note(request):
    read = request.GET.get('read')
    note_detail = Note.objects.filter(id=read)
    c_form = CommentForm()
    return render(request, 'blog-post.html', locals())


def submit_comment(request):
    comment_form = CommentForm(request.POST, request.FILES)
    path = request.META.get('HTTP_REFERER')
    read = request.POST.get('note_id')

    if request.method == 'POST':
        if comment_form.is_valid:
            instance = comment_form.save(commit=False)
            instance.note_id = read
            instance.poster = request.user.username
            if 'uploads' in request.FILES:
               instance.uploads = request.FILES['uploads']
            comment_form.save()
        else:
            return HttpResponseRedirect(path, {'c_form': comment_form})
    else:
        pass
    return HttpResponseRedirect(path)

"""
def file_download(request):
    # do something...

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = "big_file.pdf"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response

"""

def file_download(request):
    # do something...
    file_name = BASE_DIR + request.GET['url']
    print('______________________')
    with open('file_name.txt') as f:
        c = f.read()
    return HttpResponse(c)


def test(request):
    return render(request, 'testblock.html')
