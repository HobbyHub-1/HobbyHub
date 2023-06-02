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
    content = models.CharField(max_length=300)
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
    address = models.CharField(max_length=200)
    content = models.CharField(max_length=300)
    hits = models.PositiveIntegerField(default=0)

    day_choices = (('Mon', '월'), ('TUES', '화'), ('WED', '수'), ('THU', '목'), ('FRI', '금'), ('SAT', '토'), ('SUN', '일'))
    day = models.CharField(max_length=10, choices=day_choices)
    
    region_choices = (('Seoul', '서울'), ('Incheon', '인천'), ('gyeonggi-do', '경기도'), ('Gangwon-do', '강원도'), 
                      ('Gyeong-nam', '경남'), ('Gyeong-buk', '경북'), ('Jeon-nam', '전남'), ('Jeon-buk', '전북'), ('Chung-nam', '충남'), ('Chung-buk', '충북'))
    region = models.CharField(max_length=20, choices=region_choices)

    gender_choices = (('unisex', '남/여'), ('male', '남'), ('female', '여'))
    gender = models.CharField(max_length=10, choices=gender_choices)
    
    Propensity_choices = (('act', '활동적'), ('inact', '비활동적'))
    Propensity = models.CharField(max_length=10, choices=Propensity_choices)
    
    category_choices = (('sports', '운동 스포츠'), ('DIY', 'DIY 공예'), ('reading study', '독서 공부'), ('art music movie','미술 음악 영화'), ('Healing', '힐링'), ('cook', '요리'), ('Cultural activities', '문화 활동'))
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
