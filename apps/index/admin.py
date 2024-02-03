from django.contrib import admin
from .models import Country, StepbyStep, Excluded


@admin.register(Country)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', "title_en")


@admin.register(StepbyStep)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', "title_ru")


@admin.register(Excluded)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', "title_ru")
# Register your models here.