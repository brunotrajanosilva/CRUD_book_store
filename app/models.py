from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    name = models.CharField(max_length=50)
    pages = models.IntegerField()

class Order(models.Model):
    pub_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)

