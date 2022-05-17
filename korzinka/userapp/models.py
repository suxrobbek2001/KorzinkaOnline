from django.contrib.auth.models import User
from django.db import models

class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    rasm = models.FileField(blank=True, upload_to="rasmlar")
    manzil = models.CharField(max_length=80)
    zipcode = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.ism
