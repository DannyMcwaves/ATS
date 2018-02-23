from django.db import models
__all__ = ['TrackData']


class TrackData(models.Model):

    username = models.CharField(max_length=255, blank=False, unique=True)
    job_description = models.TextField(blank=False)
    resume = models.FileField(upload_to='uploads/')
    resume_words = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "__{}__".format(self.username)
