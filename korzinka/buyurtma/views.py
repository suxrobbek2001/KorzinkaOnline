from django.shortcuts import render, redirect
from django.views import View

from buyurtma.models import Bolim, Mahsulot, Sharh

from userapp.models import Mijoz


class Catalog(View):
    def get(self, request):
        bolim = Bolim.objects.all()
        return render(request, 'catalog.html', {"bolimlar": bolim})

class Mahsulotlar(View):
    def get(self, request, pk):
        bl = Bolim.objects.all()
        b = Bolim.objects.get(id=pk)
        m = Mahsulot.objects.filter(bolim=b)
        return render(request, "milkandegg.html", {"mahsulotlar": m, "bolim": b, "bolimlar": bl})

class Mahsulot_all(View):
    def get(self, request, pk):
        m = Mahsulot.objects.get(id=pk)
        mah = Mahsulot.objects.filter(bolim=m.bolim)[:4]
        aksiya = Mahsulot.objects.filter(aksiya__gte=1).order_by('-aksiya')[:4]
        for i in aksiya:
            try:
                i.narx = int(i.narx - (i.narx*i.aksiya//100))
            except:
                continue

        sh = Sharh.objects.filter(mahsulot=m)
        return render(request, "butter.html", {"mahsulot": m, "sharhlar": sh, "mah": mah, "aksiya": aksiya})

    def post(self, request, pk):
        mijoz = Mijoz.objects.get(id=1)
        m = Mahsulot.objects.get(id=pk)
        sh = Sharh.objects.filter(mahsulot=m)
        Sharh.objects.create(
            matn=request.POST['sh'],
            baho=request.POST['rating'],
            mijoz=mijoz,
            mahsulot=m
        )
        return redirect("butter", pk)



