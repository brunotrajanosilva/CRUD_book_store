from django.db import models
import uuid


# class TimeStamp(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

class User(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    name = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '%s' % (self.name)

class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ManyToManyField(Book)