from django.db import models
from django.db.models.fields import IntegerField


class Resume(models.Model):
    file = models.FileField(upload_to='resume/')


class Detail(models.Model):
    url = models.URLField(blank=False)
    img = models.TextField(blank=False, max_length=20, default='link')


class PriorityTag(models.Model):
    name = models.TextField(blank=False, max_length=20, primary_key=True)
    value = models.PositiveIntegerField(blank=False, default=1)


class Item(models.Model):
    title = models.TextField(blank=False, max_length=20)
    priority = models.ForeignKey(
        PriorityTag, on_delete=models.PROTECT, blank=False)
    url = models.TextField(default='/?page=', editable=False,
                           primary_key=True, blank=False)
    img = models.TextField(blank=False, max_length=20, default='link')

    def save(self, *args, **kwargs):
        self.url = '/?page=' + self.title
        super().save(*args, **kwargs)


class Post(models.Model):
    posttype = models.ForeignKey(Item, on_delete=models.PROTECT, blank=False)
    priority = models.ForeignKey(
        PriorityTag, on_delete=models.PROTECT, blank=False)
    title = models.TextField(blank=True, max_length=100)
    date = models.DateField(blank=True, null=True)
    body = models.TextField(blank=True)
