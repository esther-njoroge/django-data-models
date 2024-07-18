from django.db import models

# Create your models here.

class ClassPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    course = models.CharField(max_length = 20)
    classroom = models.CharField(max_length = 20)
    day_of_the_week = models.DateTimeField()


    def __str__(self):
        return f"{self.course}"

