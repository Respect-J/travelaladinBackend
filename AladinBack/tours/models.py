from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tours(BaseModel):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    mainimg = models.FileField(upload_to='tours/')
    description = models.TextField(null=True, blank=True)
    price = models.CharField(null=True, blank=True),


class Days(BaseModel):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)


class ComesOut(BaseModel):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)







