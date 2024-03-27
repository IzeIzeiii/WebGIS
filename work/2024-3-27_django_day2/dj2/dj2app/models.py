from django.db import models

"""部门表"""
class Department(models.Model):
    name=models.CharField(verbose_name='部门名',max_length=32)

""""员工表"""
class Employee(models.Model):
    name=models.CharField(verbose_name='员工姓名',max_length=16)
    psw=models.CharField(verbose_name='密码',max_length=64)
    age=models.IntegerField(verbose_name='年龄')

    gender_choices=((1,'男'),(2,'女'))
    sex=models.SmallIntegerField(verbose_name='性别',choices=gender_choices)

    salary=models.DecimalField(verbose_name='薪资',decimal_places=2,default=4000,max_digits=10)
    hiredate=models.DateTimeField(verbose_name='入职时间')
    # depart=models.ForeignKey(to="Department",to_field="id",on_delete=models.CASCADE)
    depart=models.ForeignKey(to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)