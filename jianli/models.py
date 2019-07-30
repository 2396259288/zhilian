from django.db import models

# Create your models here.
class BadsicInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    sex = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    school = models.CharField(max_length = 50)
    prof = models.CharField(max_length = 50)
    intro = models.TextField()
    honor = models.TextField()
    want_salary = models.CharField(max_length = 50, default = '')
    want_position = models.CharField(max_length = 50, default = '')
    username = models.CharField(max_length = 50, default = '')


class ProExper(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    start_date = models.CharField(max_length = 255)
    end_date = models.CharField(max_length = 255)
    info = models.TextField()
    main_work = models.TextField(default = '')
    username = models.CharField(max_length = 50, default = '')


class WorkExper(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length = 255, default = '')
    position = models.CharField(max_length = 50, default = '')
    salary = models.CharField(max_length = 50, default = '')
    start_date = models.CharField(max_length = 255)
    end_date = models.CharField(max_length = 255)
    info = models.TextField()
    honor = models.TextField(default = '')
    username = models.CharField(max_length = 50, default = '')



class jianli(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 50, default = '')
    jianli = models.CharField(max_length = 50, default = '')