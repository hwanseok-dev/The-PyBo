from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    # User.question_set과 같이 User 모델을 통해 Question 데이터에 접근할 경우
    # author 필드를 기준으로 할지 voter 필드를 기준으로 할지 장고는 알 수 없으므로 직접 정하라는 뜻이다
    # user.author_question.all()
    # user.voter_question.all()로 접근이 가능하도록 수정하였다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    # 한 개의 글에 여러 명이 추천할 수 있고,
    # 1명이 여러 개의 글을 추천할 수 있다.
    voter = models.ManyToManyField(User, related_name='voter_question')  # voter 추가

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    voter = models.ManyToManyField(User, related_name='voter_answer')