from django.contrib import admin
from .models import Tours, ComesOut, Days, DateTours, ToursImg, PriceFor


@admin.register(Tours)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', "title_en")


@admin.register(PriceFor)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('price_for_one_bussines', "price_for_two_bussines")



@admin.register(ComesOut)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('description_ru', "description_en")


@admin.register(Days)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('description_ru', "description_en")


@admin.register(DateTours)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('day_ru', "day_en")


class ToursImgAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValueError as e:
            self.message_user(request, f'Ошибка сохранения: {e}', level='ERROR')


admin.site.register(ToursImg, ToursImgAdmin)
