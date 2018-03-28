from django.db import models

# Create your models here.
class Person(models.Model):
    # id = models.AutoField(primary_key=True)#自增主键字段
    firstName = models.CharField(max_length=30, db_column="first_name")
    lastName = models.CharField(max_length=30, db_column="last_name")
    #choice
    class Meta:
        db_table = 't_person'#表名
        verbose_name=''#指定在admin管理界面中显示的名称
        # ordering = ['first_name']#排序







