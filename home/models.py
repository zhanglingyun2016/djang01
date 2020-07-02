from django.db import models

# Create your models here.



# 定义学生模型
class stu(models.Model):
    name = models.CharField(max_length=11)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)


# 定义学生详情模型
class stuinfo(models.Model):
    #创建一对一的模型关系               # 是否影响删除
    sid = models.OneToOneField(stu,on_delete=models.CASCADE)
    address = models.CharField(max_length=11)
    xueli = models.CharField(max_length=11)