from celery import shared_task
from .models import Student
import datetime as dt


days = 1


@shared_task
def set_students_to_default():
    for student in Student.objects.all():
        student.is_late = False
        student.is_missing = 0
        student.is_passing = False
        student.save()

    delta = dt.datetime.utcnow() + dt.timedelta(days=days)

    set_students_to_default.apply_async(eta=delta)


# from students.tasks import set_students_to_default
# set_students_to_default.delay()
