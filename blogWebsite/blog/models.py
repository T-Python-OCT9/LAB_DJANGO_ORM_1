from django.db import models

class Bolg(models.Model):
    title = models.CharField(max_length = 512)
    Content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField()