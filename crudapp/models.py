from django.db import models

# Create your models here.

class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    Sub1 = models.IntegerField()
    Sub2 = models.IntegerField()

