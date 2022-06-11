from django.db import models


from django.utils import timezone

# Create your models here.

class Word(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    detailed = models.CharField(max_length=500, blank=True, null=True)

    updated = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Verse(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    shown_title = models.CharField(max_length=100, blank=True, null=True)
    verse = models.CharField(max_length=500, blank=True, null=True)
    mp_verse = models.TextField(max_length=500, blank=True, null=True)

    updated = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
