from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=64)
    is_late = models.BooleanField(default=False)
    is_missing = models.SmallIntegerField(default=0)
    is_passing = models.BooleanField(default=False)
    tg_id = models.SmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
