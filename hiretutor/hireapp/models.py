from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_guardian = models.BooleanField(default=False)


class TutorProfiles(models.Model):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Your_Full_Name = models.CharField(max_length=50)
    Fathers_Name = models.CharField("Father's Name", max_length=50)
    Mothers_Name = models.CharField("Mother's Name",max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.CharField(max_length=3)
    Date_of_Birth = models.DateField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    address = models.TextField(max_length=150)
    nid_No = models.CharField(max_length=18)
    tution_you_give_to_class = models.CharField(max_length=2)
    subjects_you_teach = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    need_tution_from = models.DateField()
    fees_per_subject = models.CharField(max_length=5)
    week = models.CharField("How many days you are available?", max_length=1)
    tution_hour = models.CharField(max_length=2)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.Your_Full_Name

    def get_queryset(self):
        return TutorProfiles.objects.all()


class GuardianProfiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=20)
    image = models.ImageField(upload_to='', blank=True, null=True)
    g_or_t = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_queryset(self):
        return GuardianProfiles.objects.all()
