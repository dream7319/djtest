from django.db import models

# Create your models here.

"""
Django不允许下面两种字段名:
1、与Python关键字冲突。这会导致语法错误。例如：
    class Example(models.Model): pass = models.IntegerField() # 'pass'是Python保留字！
2、字段名中不能有两个以上下划线在一起，因为两个下划线是Django的查询语法。例如：
    class Example(models.Model): foo__bar = models.IntegerField() # 'foo__bar' 有两个下划线在一起!
"""
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()




