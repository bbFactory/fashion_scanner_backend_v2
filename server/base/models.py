
from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(unique=True, primary_key=True, auto_created=True, verbose_name="Primary ID")
    createdAt = models.DateTimeField(null=True)
    updatedAt = models.DateTimeField(null=True)

    class Meta:
        ordering = ('pk',)
        abstract = True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
