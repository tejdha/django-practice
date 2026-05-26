from django.db import models

# Create your models here.
class user(models.Model):
    id = models.IntegerField(primary_key=1)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.id} , {self.uname}<br>'
