
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']