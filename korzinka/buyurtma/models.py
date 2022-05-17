from django.db import models
from userapp.models import Mijoz


class Bolim(models.Model):
    nom = models.CharField(max_length=150)
    rasm = models.FileField(upload_to="bolim_rasmi")

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    batafsil = models.CharField(max_length=350)
    rasm = models.FileField(upload_to="mahsulot_rasmi")
    brend = models.CharField(max_length=50)
    mamlakat = models.CharField(max_length=50)
    vazn = models.CharField(max_length=50)
    narx = models.IntegerField()
    mavjud = models.BooleanField(default=True)
    aksiya = models.CharField(max_length=10, blank=True, default=0)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nom} {self.brend},{self.vazn}"

class Sharh(models.Model):
    baho = models.PositiveIntegerField(default=0)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    matn = models.CharField(max_length=400)
    sana = models.DateField(auto_now_add=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.matn
