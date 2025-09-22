from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    student_class=models.CharField(max_length=20)
    age=models.PositiveIntegerField()

    def __str__(self):
        return self.name
