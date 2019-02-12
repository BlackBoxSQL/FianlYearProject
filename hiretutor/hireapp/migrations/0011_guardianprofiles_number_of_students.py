# Generated by Django 2.0 on 2019-02-12 02:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hireapp', '0010_guardianprofiles_week_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardianprofiles',
            name='number_of_students',
            field=models.CharField(default=django.utils.timezone.now, max_length=2, verbose_name='Number of students'),
            preserve_default=False,
        ),
    ]
