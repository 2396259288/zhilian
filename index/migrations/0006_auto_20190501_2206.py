# Generated by Django 2.1.7 on 2019-05-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20190501_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobinfo',
            name='info',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='jobinfoclik',
            name='info',
            field=models.TextField(default=''),
        ),
    ]
