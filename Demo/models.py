from django.db import models


class Details(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    phoneNumber = models.CharField(max_length=255, blank=True, null=True)

class Slots(models.Model):
    slots = models.CharField(max_length=255550,blank=True,null=True)
