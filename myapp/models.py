from django.db import models

# Create your models here.
class Person(models.Model):
    firstName = models.CharField(max_length=30,db_column="first_name")
    lastName = models.CharField(max_length=30,db_column="last_name")