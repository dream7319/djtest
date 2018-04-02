from django.db import models

#python manage.py makemigrations myapp
#python manage.py migrate myapp
# Create your models here.
class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女')
    )
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    #性别使用了一个choice，只能选择男或者女，默认为男；
    sex = models.CharField(max_length=10,choices=gender, default='男')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "t_user"
        ordering = ["-create_time"]
        verbose_name = "用户"
        verbose_name_plural="用户"

