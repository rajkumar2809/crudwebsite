from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class signup_user(models.Model):

    name = models.CharField(max_length=100,blank=True)
    contact_no = models.IntegerField(unique=False,blank=True,null=True)
    roll_no = models.IntegerField(unique=False,blank=True,null=True)
    subject = models.CharField(max_length=200,blank=True)
    added_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name + " " + str(self.roll_no)

    class Meta:
        verbose_name_plural = "Contact Us"


