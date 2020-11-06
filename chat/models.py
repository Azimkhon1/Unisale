from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Messages(models.Model):  # class Messages 
    """Model for chatting"""
    text = models.CharField(max_length=500),  # text VARCHAR(500)
    pub_date = models.DateTimeField(auto_now_add=True)  # making published date
    status = models.BooleanField()  # status read not unread
    user_to = models.ForeignKey(User, on_delete=models.PROTECT),  # to the user
    user_from = models.ForeignKey(User, on_delete=models.PROTECT)   # from the user
