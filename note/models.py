from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField('标签', max_length=20)


class Note(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容', max_length=10000)
    update_time = models.DateTimeField('更新日期', auto_now=True)
    views = models.IntegerField('浏览数', default=1, blank=True)
    poster_id = models.CharField('作者', max_length=100, default=1, blank=True)
    original_url = models.URLField(blank=True)
    display = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name_plural = '学习笔记'
        ordering = ['-update_time']


class Comment(models.Model):
    poster = models.CharField('姓名', max_length=100)
    post_time = models.DateTimeField('时间', auto_now=True)
    comment = models.TextField('', max_length=2000)
    note = models.ForeignKey(Note)
    display = models.BooleanField(default=1)
    uploads = models.FileField('附件',upload_to='note/%Y%m%d', blank=True)


    class Meta:
        verbose_name_plural = '评论'

    def __str__(self):
        return self.comment
