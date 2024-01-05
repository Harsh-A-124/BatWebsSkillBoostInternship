from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=30)
    age = models.IntegerField()
    contactno = models.BigIntegerField()
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=40)
    college = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    sscm = models.IntegerField()
    hscm = models.IntegerField()

    def __str__(self):
        return self.fullname