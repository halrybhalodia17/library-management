from django.db import models
from student.models import StudentDb

# Create your models here.
class LibrarianDb(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(primary_key = True)
    password = models.CharField(max_length=20)


class Books(models.Model):
    name = models.CharField(max_length=200, unique = True)
    author = models.CharField(max_length=200)
    total = models.IntegerField()

class IssueReturn(models.Model):
    email = models.ForeignKey(StudentDb, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    issue_date = models.DateField()
    return_date = models.DateField()
    fine = models.IntegerField(default = 0)
