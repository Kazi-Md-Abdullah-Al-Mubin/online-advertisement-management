from django.db import models


class User(models.Model):
    id = models.IntegerField
    device = models.CharField(max_length=30)
    os = models.CharField(max_length=20)
    browser = models.CharField(max_length=20)
    time = models.CharField(max_length=30)
    site_type = models.CharField(max_length=40)




