from django.db import models
from django.urls import reverse

class Task(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title[:25]
    
    def get_absolute_url(self):
        return reverse('home')

