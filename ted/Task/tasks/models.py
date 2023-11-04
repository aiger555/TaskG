from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Task(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.AutoField()

    def get_absolute_url(self):
        return reverse('task_detail_url', kwargs={'id': self.id})

    def get_create_url(self):
        return reverse('task_create_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('task_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('task_delete_url', kwargs={'id': self.id})


