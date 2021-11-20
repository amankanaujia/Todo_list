from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title