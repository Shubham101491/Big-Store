from django.db import models
from django.contrib.auth.models import User


class Register(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)

    