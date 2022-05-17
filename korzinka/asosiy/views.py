from django.shortcuts import render
from django.views import View


from asosiy.models import Maqola

from buyurtma.models import Bolim, Mahsulot


class Index(View):
    def get(self, request):
        maqola = Maqola.objects.all()
        bolim = Bolim.objects.all()
        aksiya = Mahsulot.objects.filter(aksiya__gte=1).order_by('-aksiya')[:4]
        yangi = Mahsulot.objects.all().order_by("-id")[:4]
        oldin = Mahsulot.objects.all().order_by('?')[:4]
        return render(request, 'index.html', {"maqola": maqola, "bolimlar": bolim, "aksiya": aksiya, "yangi": yangi, "oldin": oldin})

class Savat(View):
    def get(self, request):
        bolim = Bolim.objects.all()
        return render(request, 'basket.html', {"bolimlar": bolim})

class Tanlangan(View):
    def get(self, request):
        bolim = Bolim.objects.all()
        return render(request, 'izbranny.html', {"bolimlar": bolim})

class Buyurtma(View):
    def get(self, request):
        bolim = Bolim.objects.all()
        return render(request, "orders.html", {"bolimlar": bolim})