from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Sharh, Mahsulot, Bolim
admin.site.register(Sharh)
admin.site.register(Bolim)

@admin.register(Mahsulot)
class MahsulotAdmin(ModelAdmin):
    search_fields = ['nom', 'brend']
