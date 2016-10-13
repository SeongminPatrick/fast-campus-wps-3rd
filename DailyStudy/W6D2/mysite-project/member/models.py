from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# 커스텀 유저를 만들어보자
class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    # 규약 새로운 모델을 만들때 장고에게 어떤 값을 유저 네밍으로 할껀지 알려줌
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ('email',)