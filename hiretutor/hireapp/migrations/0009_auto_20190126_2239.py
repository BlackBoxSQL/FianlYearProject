# Generated by Django 2.0 on 2019-01-26 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireapp', '0008_auto_20190126_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardianprofiles',
            name='tution_hour',
            field=models.CharField(max_length=3, verbose_name='Tution hours'),
        ),
        migrations.AlterField(
            model_name='tutorprofiles',
            name='tution_hour',
            field=models.CharField(max_length=3),
        ),
    ]