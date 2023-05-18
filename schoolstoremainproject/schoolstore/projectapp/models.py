from django.db import models

# Create your models here.
class form(models.Model):
    NAME = models.CharField(max_length=150)
    DOB = models.DateField()
    Age = models.IntegerField()
    Gender = models.CharField(max_length=50)
    Phonenumber = models.IntegerField()
    Mailid = models.EmailField()
    Address = models.TextField()
    Department = models.CharField(max_length=150)
    Courses = models.CharField(max_length=200)
    Purpose = models.CharField(max_length=200)
    Materialsprovide = models.CharField(max_length=200)


    def __str__(self):
        return self.NAME





