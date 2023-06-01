#accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from posts.models import Group

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    password = models.CharField(max_length=30)

    profile_image = ProcessedImageField(blank=True,
                                        upload_to='users',
                                        processors=[ResizeToFill(200, 200)],
                                        format='JPEG',
                                        options={'quality': 70})
    def liked_groups(self):
        return Group.objects.filter(like_users=self)
    


# 심리 테스트 질문 question_text 필드는 질문의 텍스트를 저장하고 answer_choices 필드는 질문에 대한 답변 선택지를 저장
# class Question(models.Model):
#     question_text = models.CharField(max_length=255)
#     answer_choices = models.CharField(max_length=255)


# 사용자의 심리 테스트 질문에 대한 응답 question 필드는 응답이 속한 질문을 가리키고 user 필드는 응답을 한 사용자, answer_choice 필드는 응답한 답변 선택지를 저장
# class Response(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     answer_choice = models.CharField(max_length=255)


# 사용자에게 취미 추천
# class Recommendation(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)


# 취미
# class Hobby(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()