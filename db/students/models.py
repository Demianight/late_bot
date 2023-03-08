from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=64)
    is_late = models.BooleanField()
    is_missing = models.SmallIntegerField()
    is_passing = models.BooleanField()
    tg_id = models.SmallIntegerField()
