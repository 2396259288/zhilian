# Generated by Django 2.1.7 on 2019-04-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BadsicInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('prof', models.CharField(max_length=50)),
                ('intro', models.TextField()),
                ('honor', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProExper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=255)),
                ('end_date', models.CharField(max_length=255)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=255)),
                ('end_date', models.CharField(max_length=255)),
                ('info', models.TextField()),
            ],
        ),
    ]
