from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    # User 모델에서 정보를 가져옴
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # auto_now_add 로 생성시간을 자동 삽입
    create_date = models.DateTimeField(auto_now_add=True)
    # default 가 blank
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # 퍼블리시 하면 현재시간이 들어간다
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
