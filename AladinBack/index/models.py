from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True)
    img = models.FileField(upload_to='country/')
    description = models.TextField(null=True, blank=True)


class Tours(BaseModel):
    pass


class StepbyStep(BaseModel):
    title = models.CharField(max_length=512, null=True, blank=True)



