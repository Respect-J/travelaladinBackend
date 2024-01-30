from django.contrib import admin
from .models import Tours, ComesOut, Days, DateTours


@admin.register(Tours)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', "title_en")


@admin.register(ComesOut)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('description_ru', "description_en")


@admin.register(Days)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('description_ru', "description_en")


@admin.register(DateTours)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('day_ru', "day_en")