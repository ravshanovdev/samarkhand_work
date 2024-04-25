from django.db import models
from django.contrib.auth.models import User

VALUE_TYPE6 = (
    ("ona tili", "Ona Tili"),

)

VALUE_TYPE7 = (
    ("ingiliz tili", "ingiliz Tili"),

)

VALUE_TYPE8 = (
    ("fransuz", "Fransuz"),
    ("nemis", "Nemis")

)

VALUE_TYPE = (
    ("maktabni bitirganman", "Maktabni Bitirganman"),
    ("maktabda o'qiyman", "Maktabda O'qiyman")

)

VALUE_TYPE2 = (
    ("qashqadaryo", "Qashqadaryo"),

)

VALUE_TYPE3 = (
    ("shahrisabz", "Shahrisabz"),

)

VALUE_TYPE4 = (
    ("15-maktab", "15-Maktab"),

)

VALUE_TYPE5 = (
    ("a", "A"),

)

VALUE_TYPE9 = (
    ("1-snif", "1-Snif"),

)


class MyResume(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    birthday = models.CharField(max_length=10)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=20, choices=VALUE_TYPE)
    viloyat = models.CharField(max_length=20, choices=VALUE_TYPE2)
    tuman = models.CharField(max_length=20, choices=VALUE_TYPE3)
    maktab = models.CharField(max_length=20, choices=VALUE_TYPE4)
    snif = models.CharField(max_length=20, choices=VALUE_TYPE9)
    harf = models.CharField(max_length=20, choices=VALUE_TYPE5)
    one_tili = models.CharField(max_length=20, choices=VALUE_TYPE6)
    ingiliz_tili = models.CharField(max_length=20, choices=VALUE_TYPE7)
    boshqa_til = models.CharField(max_length=20, choices=VALUE_TYPE8)

# Test:
#  - title,
#  - description,
#  - image,
#  - variants ( Variants Model ),
#  - answer ( Variants Model )


class Variants(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    right_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    variants = models.ManyToManyField('Variants', blank=True, related_name='test_variants')
    answer = models.ForeignKey(Variants, on_delete=models.CASCADE, related_name='test_answer')

    def __str__(self):
        return self.title












