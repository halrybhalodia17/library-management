from django.db import models

# Create your models here.

class StudentDb(models.Model):
    enroll_no = models.IntegerField(unique = True)
    name = models.CharField(max_length=25)
    email = models.EmailField(primary_key=True)
    branch = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    password = models.CharField(max_length=20)
    roll_no = models.IntegerField()
    shift = models.CharField(max_length=20)