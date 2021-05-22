from user.models import User
from model_abs import ModelAbs
from django.db import models


class Task(ModelAbs):
    title = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)

class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    image = models.FileField(blank=True)