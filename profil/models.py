from django.db import models
from django.contrib.auth.models import User

VALUE_TYPE2 = (
    ("qashqadaryo", "Qashqadaryo"),

)

VALUE_TYPE3 = (
    ("shahrisabz", "Shahrisabz"),

)

VALUE_TYPE4 = (
    ("15-maktab", "15-Maktab"),

)

VALUE_TYPE9 = (
    ("1-snif", "1-Snif"),

)

VALUE_TYPE5 = (
    ("a", "A"),

)


class MyProfil(models.Model):
    username = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    viloyat = models.CharField(max_length=20, choices=VALUE_TYPE2)
    tuman = models.CharField(max_length=20, choices=VALUE_TYPE3)
    maktab = models.CharField(max_length=20, choices=VALUE_TYPE4)
    snif = models.CharField(max_length=20, choices=VALUE_TYPE9)
    harf = models.CharField(max_length=20, choices=VALUE_TYPE5)

