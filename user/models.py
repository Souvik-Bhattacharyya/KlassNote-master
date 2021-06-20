from django.db import models
from django.contrib.auth.models import User


class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField(default=100000, null=False)
