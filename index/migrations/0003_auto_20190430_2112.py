# Generated by Django 2.1.7 on 2019-04-30 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20190430_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobinfo',
            name='info',
        ),
        migrations.RemoveField(
            model_name='jobinfoclik',
            name='info',
        ),
    ]
