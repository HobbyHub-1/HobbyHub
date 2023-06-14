#posts/models.py

from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager
from django.utils import timezone
from datetime import timedelta,datetime
# from django.core.validators import RegexValidator
# from django.core.validators import MinValueValidator, MaxValueValidator
import os

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, default='')
    content = models.CharField(max_length=100000)
    hits = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=20)
    tags = TaggableManager(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='hobby', blank=True,
                                processors=[ResizeToFill(400,400)],
                                format='JPEG',
                                options={'quality': 100})


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def created_string(self):
        if self.created_at is None:
            return False

        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False


class Group(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_group')
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    hits = models.PositiveIntegerField(default=0)

    day_choices = (('월요일', '월요일'), ('화요일', '화요일'), ('수요일', '수요일'), ('목요일', '목요일'), ('금요일', '금요일'), ('토요일', '토요일'), ('링요일', '일요일'))
    day = models.CharField(max_length=10, choices=day_choices)
    
    region_choices = (('서울', '서울'), ('인천', '인천'), ('경기도', '경기도'), ('강원도', '강원도'), 
                      ('경남', '경남'), ('경북', '경북'), ('전남', '전남'), ('전북', '전북'), ('충남', '충남'), ('충북', '충북'))
    region = models.CharField(max_length=20, choices=region_choices)

    gender_choices = (('남/여', '남/여'), ('남', '남'), ('여', '여'))
    gender = models.CharField(max_length=10, choices=gender_choices)
    
    propensity_choices = (('활동적', '활동적'), ('비활동적', '비활동적'))
    propensity = models.CharField(max_length=10, choices=propensity_choices, null=True)
    
    category_choices = (('운동 스포츠', '운동 스포츠'), ('DIY 공예', 'DIY 공예'), ('독서 공부', '독서 공부'), ('미술 음악 영화','미술 음악 영화'), ('힐링', '힐링'), ('요리', '요리'), ('문화 활동', '문화 활동'))
    category = models.CharField(max_length=20, choices=category_choices)
    
    tags = TaggableManager(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title
    
    
# class Category(models.Model):
#    name = models.CharField(max_length=100)

 #   def __str__(self):
  #      return self.name


class GroupImage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='group', blank=True,
                                processors=[ResizeToFill(400,400)],
                                format='JPEG',
                                options={'quality': 100})
    

class GroupComment(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def created_string(self):
        if self.created_at is None:
            return False

        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False
