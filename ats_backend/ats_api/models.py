from django.db import models
__all__ = ['TrackData']


class TrackData(models.Model):

    description = models.TextField(blank=False)
    resume = models.FileField(upload_to='uploads/')
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
