from django.db import models

class Video(models.Model):
    add_date = models.DateTimeField(auto_now_add=True)
    kind = models.CharField(max_length=100)
    youtube_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    published_date = models.DateTimeField()
    thumbnail_url = models.URLField(blank=True)


    def __str__(self):
        return self.title