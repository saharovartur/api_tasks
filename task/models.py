from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название задачи', blank=False)
    is_completed = models.BooleanField(default=False, verbose_name='Выполнено')
