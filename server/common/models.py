from django.db import models
from server.base.models import BaseModel

# Create your models here.


class Color(BaseModel):
    hex_code = models.CharField(max_length=6, unique=True, verbose_name="색상 코드")

    def __str__(self):
        return f"{self.hex_code}({self.id})"

    class Meta:
        db_table = "color"
        verbose_name = "색상"
        verbose_name_plural = "색상"
        ordering = ["id"]
