from django.db import models  # from django.db import models module
from django.utils import timezone
from users.forms import UserRegisterForm
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):  # making a table Tag
    title = models.CharField(max_length=200)  # making a title VARCHAR

    def __str__(self):  # function to show strings instead of memory location.
        return self.title  # return strings


class Post(models.Model):  # making a table Post
    post_name = models.CharField(max_length=200)  # making post_name VARCHAR
    item = models.CharField(max_length=200)  # making item VARCHAR
    description = models.CharField(max_length=200)  # making description VARCHAR
    price = models.IntegerField()  # making price INTEGER
    dorm_choices = (
        ('Apartments', 'Apartments'),
        ('Hilltop House', 'Hilltop House'),
        ('Holmes Hall', 'Holmes Hall'),
        ('Leitzell Hall', 'Leitzell Hall'),
        ('Oyaron House', 'Oyaron House'),
        ('Pine Lake Housing', 'Pine Lake Housing'),
        ('Saxton Hall', 'Saxton Hall'),
        ('Smith Hall', 'Smith Hall'),
        ('Townhouses', 'Townhouses'),
        ('Van Ess Hall', 'Van Ess Hall'),
        ('Wilder Hall', 'Wilder Hall'),
    )
    contact_information = models.CharField(max_length=200, choices=dorm_choices)  # making contact_information VARCHAR
    pub_date = models.DateTimeField(auto_now_add=True)  # making published date
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    tags = models.ManyToManyField(Tag)  # making tags many-to-many relationship with Tag table
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  # making creator for joining
    # user's email

    def __str__(self):  # function to show strings instead of memory location.
        return self.post_name  # return strings


class Support(models.Model):
    text = models.CharField(max_length=300)
    email = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

