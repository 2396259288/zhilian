# Generated by Django 2.1.7 on 2019-05-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20190430_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinfo',
            name='companySize',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='companyType',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='info',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='welfare',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='workingExp',
            field=models.CharField(default='', max_length=255),
        ),
    ]
