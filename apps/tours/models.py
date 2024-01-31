from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tours(BaseModel):
    id = models.IntegerField(primary_key=True, unique=True)
    title_en = models.CharField(max_length=256, null=True, blank=True)
    title_ru = models.CharField(max_length=256, null=True, blank=True)
    mainimg = models.FileField(upload_to='tours/')
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    price_for_one = models.CharField(max_length=56, null=True, blank=True)
    price_for_two = models.CharField(max_length=56, null=True, blank=True)


class Days(BaseModel):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)


class ComesOut(BaseModel):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)


class DateTours(BaseModel):
    day_en = models.CharField(max_length=256, null=True, blank=True)
    day_ru = models.CharField(max_length=256, null=True, blank=True)






