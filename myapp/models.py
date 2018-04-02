from django.db import models
from datetime import timezone, timedelta, datetime
#python manage.py makemigrations myapp
#python manage.py migrate myapp
# Create your models here.
class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女')
    )
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    #性别使用了一个choice，只能选择男或者女，默认为男；
    sex = models.CharField(max_length=10,choices=gender, default='男')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    #用来区别用户是否进行了邮箱验证
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "t_user"
        ordering = ["-create_time"]
        verbose_name = "用户"
        verbose_name_plural="用户"

#保存了用户和注册码之间的关系，一对一的形式
class ConfirmString(models.Model):
    code = models.CharField(max_length=256)#哈希后的注册码
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['create_time']
        verbose_name="确认码"
        verbose_name_plural="确认码"

    def __str__(self):
        return self.user.name+": "+ self.code