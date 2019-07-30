from django.db import models

# Create your models here.
class Position(models.Model):
	position_id = models.AutoField(primary_key=True)
	position_name = models.CharField(max_length = 50)
	position_type = models.CharField(max_length = 50)
	position_trade = models.CharField(max_length = 50)




class JobInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    salary = models.CharField(max_length = 255)
    companyName = models.CharField(max_length = 255)
    companySize = models.CharField(max_length = 255, default = '')
    companyType = models.CharField(max_length = 255, default = '')
    workingExp = models.CharField(max_length = 255, default = '')
    city = models.CharField(max_length = 255)
    time = models.CharField(max_length = 255)
    idName = models.CharField(max_length = 255)
    url = models.CharField(max_length = 255, default = '')
    info = models.TextField(default = '')
    clik = models.IntegerField(default = 0)
    status = models.IntegerField(default = 0)
    companyEmail = models.CharField(max_length = 255, default = '')


