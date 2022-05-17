from django.db import models
from buyurtma.models import Mahsulot
from userapp.models import Mijoz

class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    soni = models.PositiveIntegerField()
    summa = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.mahsulot}, {self.mijoz}"

class Tanlangan(models.Model):
    mahsulot = models.ManyToManyField(Mahsulot)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.mahsulot}, {self.mijoz}"

class Buyurtma(models.Model):
    savat = models.ForeignKey(Savat, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    summa = models.PositiveIntegerField()
    status = models.CharField(max_length=50, default="Jarayonda")
    vaqt = models.DateTimeField()

class Maqola(models.Model):
    title = models.CharField(max_length=350)
    description = models.CharField(max_length=400)
    matn = models.TextField()
    rasm = models.FileField(upload_to="maqola_rasmi")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title




