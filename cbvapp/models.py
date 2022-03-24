from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    

