# Generated by Django 2.1.7 on 2019-04-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jianli', '0005_auto_20190428_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='badsicinfo',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='proexper',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='workexper',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
