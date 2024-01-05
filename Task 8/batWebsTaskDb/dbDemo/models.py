from django.db import models

class Student(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    fullname = models.CharField(max_length=30)
    age = models.IntegerField()
    contactno = models.BigIntegerField()
    email = models.EmailField(max_length=200)
    college = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    sscm = models.IntegerField()
    hscm = models.IntegerField()

    def __str__(self):
        return(f"{self.fullname}")