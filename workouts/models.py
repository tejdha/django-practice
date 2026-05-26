from django.db import models

# Create your models here.
class workouts(models.Model):
    wname = models.CharField(max_length=30)
    duration = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f'{self.wname} day - {self.duration} min - {self.status} duration'