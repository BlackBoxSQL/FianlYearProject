# Generated by Django 2.0 on 2019-01-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorprofiles',
            name='week',
            field=models.CharField(max_length=1, verbose_name='How many days you are available?'),
        ),
    ]
