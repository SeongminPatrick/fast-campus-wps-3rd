from django.utils import timezone

from django.db import models
from django.conf import settings




class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




