from django.db import models

from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.


class Course(models.Model):
    Name = models.CharField(max_length=256)
    price = models.IntegerField()
    Discount = models.IntegerField()
    Duration = models.DateTimeField(default=datetime.now())
    AuthorName = models.CharField(max_length=256)
    owner = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class CourseCategory(models.Model):
    product = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="ingredients", )
    protein = models.FloatField()

    def __str__(self):
        return self.product.Name
