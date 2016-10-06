import datetime
from django.utils import timezone

from django.db import models



class Question(models.Model):
    question_text = models.CharField('질문 내용', max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # datetime.timedelt 시간의 양을 나타냄, datetime.timedelta(days=1) 하루를 나타냄
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('선택한내용', max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

