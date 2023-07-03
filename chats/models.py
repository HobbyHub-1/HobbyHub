from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

class ChatRoom(models.Model):
    participants = models.ManyToManyField(get_user_model(), related_name='chat_rooms')
    name = models.CharField(max_length=255, blank=True)

    @classmethod
    # get_or_create_chat_room은 주어진 사용자들의 채팅방을 가져오거나 생성하는 클래스 메서드
    def get_or_create_chat_room(cls, users):
        unique_users = set(users)
        if len(unique_users) == 1:
            room_name = "나(" + list(unique_users)[0].first_name + ")"
            # 주어진 사용자들이 동일한 사용자라면 "나(사용자 이름)" 형식의 이름을 사용
        else:
            room_name = ",".join(sorted([user.first_name for user in users]))
            # 그렇지 않다면 사용자들의 이름을 정렬하여 쉼표로 구분한 문자열을 이름으로 사용

        chat_room = cls.objects.filter(name=room_name).first()
        if chat_room:
            return chat_room
            # 이미 존재하는 채팅방이 있다면 해당 채팅방을 반환

        chat_room = cls.objects.create(name=room_name)
        chat_room.participants.set(unique_users)
        return chat_room
        # 존재하지 않는다면 새로운 채팅방을 생성하여 반환

    def __str__(self):
        return self.name
    

class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        if not self.is_read:
            self.is_read = True
            self.save()

    def formatted_timestamp(self):
        # self.timestamp에 대해 시간대 정보를 추가합니다.
        if self.timestamp.tzinfo is None or self.timestamp.tzinfo.utcoffset(self.timestamp) is None:
            local_timestamp = timezone.make_aware(self.timestamp, timezone.get_default_timezone())
        else:
            local_timestamp = self.timestamp

        am_pm = "오전" if local_timestamp.strftime('%p') == "AM" else "오후"
        return f"{am_pm} {local_timestamp.strftime('%I:%M')}"
    

class Notification(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def mark_as_read(self):
        if not self.is_read:
            self.is_read = True
            self.save()

    def formatted_timestamp(self):
        # self.timestamp에 대해 시간대 정보를 추가합니다.
        if self.timestamp.tzinfo is None or self.timestamp.tzinfo.utcoffset(self.timestamp) is None:
            local_timestamp = timezone.make_aware(self.timestamp, timezone.get_default_timezone())
        else:
            local_timestamp = self.timestamp

        am_pm = "오전" if local_timestamp.strftime('%p') == "AM" else "오후"
        return f"{am_pm} {local_timestamp.strftime('%I:%M')}"


    @classmethod
    def delete_old_notifications(cls):
        one_week_ago = timezone.now() - timezone.timedelta(days=7)
        cls.objects.filter(timestamp__lt=one_week_ago).delete()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.delete_old_notifications()