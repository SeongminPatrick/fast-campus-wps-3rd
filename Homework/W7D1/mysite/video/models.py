from django.db import models

class Video(models.Model):
    # createdDate = models.DateTimeField(auto_now_add=True)
    kind = models.CharField(max_length=100)
    videoId = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    publishedAt = models.DateTimeField()
    thumbnails = models.URLField(blank=True)

    def __str__(self):
        return self.title