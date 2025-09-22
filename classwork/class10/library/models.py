from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.TextField()
    year = models.DecimalField(max_digits=10, decimal_places=2)