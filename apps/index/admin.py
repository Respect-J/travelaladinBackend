from django.contrib import admin
from .models import Country, StepbyStep, Excluded, Contact


@admin.register(Country)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', "title_en")


@admin.register(StepbyStep)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', "title_ru")


@admin.register(Excluded)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', "title_ru")


@admin.register(Contact)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('number_uz', "number_ru")
