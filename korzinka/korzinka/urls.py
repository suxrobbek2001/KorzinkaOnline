from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from buyurtma.views import Catalog, Mahsulotlar, Mahsulot_all
from asosiy.views import Index, Savat, Tanlangan, Buyurtma

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('basket/', Savat.as_view(), name="basket"),
    path('izbranny/', Tanlangan.as_view(), name="izbranny"),
    path('orders/', Buyurtma.as_view(), name="orders"),
    path('catalog/', Catalog.as_view(), name="catalog"),
    path('catalog/<int:pk>/', Mahsulotlar.as_view(), name="mahsulotlar"),
    path('butter/<int:pk>/', Mahsulot_all.as_view(), name="butter"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)