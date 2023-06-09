# Generated by Django 3.2.18 on 2023-06-15 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(default='', max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=2000)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('day', models.CharField(choices=[('월요일', '월요일'), ('화요일', '화요일'), ('수요일', '수요일'), ('목요일', '목요일'), ('금요일', '금요일'), ('토요일', '토요일'), ('일요일', '일요일')], max_length=10)),
                ('region', models.CharField(choices=[('서울', '서울'), ('인천', '인천'), ('경기도', '경기도'), ('강원도', '강원도'), ('경남', '경남'), ('경북', '경북'), ('전남', '전남'), ('전북', '전북'), ('충남', '충남'), ('충북', '충북')], max_length=20)),
                ('gender', models.CharField(choices=[('남/여', '남/여'), ('남', '남'), ('여', '여')], max_length=10)),
                ('propensity', models.CharField(choices=[('활동적', '활동적'), ('비활동적', '비활동적')], max_length=10, null=True)),
                ('category', models.CharField(choices=[('운동 스포츠', '운동 스포츠'), ('DIY 공예', 'DIY 공예'), ('독서 공부', '독서 공부'), ('미술 음악 영화', '미술 음악 영화'), ('힐링', '힐링'), ('요리', '요리'), ('문화 활동', '문화 활동')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_users', models.ManyToManyField(related_name='like_group', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(default='', max_length=100)),
                ('content', models.CharField(max_length=100000)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_users', models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='hobby')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='group')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.group')),
            ],
        ),
        migrations.CreateModel(
            name='GroupComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
