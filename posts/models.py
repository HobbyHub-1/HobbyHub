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
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    content = models.CharField(max_length=300)
    hits = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=20)
    tags = TaggableManager(blank=True)

    thumbnail = ProcessedImageField(upload_to='hobby', 
                                    blank=True, processors=[ResizeToFill(400,400)],
                                    format='JPEG',
                                    options={'quality': 100})

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title
    

class GroupImage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='group', blank=True,
                                processors=[ResizeToFill(400,400)],
                                format='JPEG',
                                options={'quality': 100})
    

class GroupComment(models.Model):
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
