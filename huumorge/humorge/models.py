from django.db import models
from django.utils import timezone

# Create your models here.

class FreeBoard(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def write(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class FreeComment(models.Model):
    freeboard = models.ForeignKey('FreeBoard', on_delete=models.CASCADE, related_name='free_comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def add_coment(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.content

class HumorBoard(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def write(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class HumorComment(models.Model):
    humorboard = models.ForeignKey('HumorBoard', on_delete=models.CASCADE, related_name='humor_comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def add_coment(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.content
