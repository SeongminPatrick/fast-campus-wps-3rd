from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, User

# 기존 유저에 컬럼만 추가해서 사용하는 법 (간편하다)
# https://www.youtube.com/watch?v=teY7TXhlDZA 19분

class YoutubeUserManager(UserManager):
    pass

class YoutubeUser(AbstractUser):
    nickname = models.CharField(max_length=30)

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자 목록록'


    def __str__(self):
        return self.username