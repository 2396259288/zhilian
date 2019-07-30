# Generated by Django 2.1.7 on 2019-05-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20190501_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinfoclik',
            name='companySize',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='jobinfoclik',
            name='companyType',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='jobinfoclik',
            name='info',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='jobinfoclik',
            name='welfare',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='jobinfoclik',
            name='workingExp',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='jobinfoclik',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobinfoclik',
            name='companyName',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobinfoclik',
            name='idName',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobinfoclik',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobinfoclik',
            name='salary',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobinfoclik',
            name='time',
            field=models.CharField(max_length=255),
        ),
    ]
