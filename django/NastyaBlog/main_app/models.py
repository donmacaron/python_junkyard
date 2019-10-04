from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length = 32, default = 'Стриж')
    title = models.CharField(max_length = 64, default = 'Я забыла написать название поста')
    content = models.CharField(max_length = 1500)
    date = models.DateTimeField(blank = True, null = True)


    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
