from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone # Import timezone

class Users(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(default=timezone.now) # Use timezone.now
    likes = models.ManyToManyField(Users, related_name='liked_answers', blank=True)

    def __str__(self):
        return f"Answer to '{self.question.title}' by {self.author.username}"

    @property
    def total_likes(self):
        return self.likes.count()