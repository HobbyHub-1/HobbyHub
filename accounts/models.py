#accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from posts.models import Group

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    joined_at = models.DateTimeField(auto_now_add=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    level = models.IntegerField(default=1)
    profile_image = ProcessedImageField(blank=True,
                                        upload_to='users',
                                        processors=[ResizeToFill(200, 200)],
                                        format='JPEG',
                                        options={'quality': 70})
    
    def image_path(instance, filename):
        return f'account/{instance.pk}/{filename}'
    
    def liked_groups(self):
        return Group.objects.filter(like_users=self)
    
