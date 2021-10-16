from django.db import models
from server.base.models import BaseModel
# Create your models here.


class Members(BaseModel):
    BLACKPINK = "BLACKPINK"
    BTS = "BTS"
    CHOICES_TYPE = ((BLACKPINK, "BLACKPINK"), (BTS, "BTS"))
    ko_name = models.CharField("이름", max_length=10, blank=True, null=True)
    en_name = models.CharField("영문 이름", max_length=64, blank=True, null=True)
    group_type = models.CharField("그룹 타입", max_length=64, choices=CHOICES_TYPE, blank=True, null=True, default=None)
    color = models.ForeignKey('common.Color', verbose_name="색상", on_delete=models.CASCADE)
    brand = models.ManyToManyField('common.Brand', verbose_name="브랜드")

    def __str__(self):
        return f"{self.ko_name}({self.id})"

    class Meta:
        db_table = "member_members"
        verbose_name = "멤버"
        verbose_name_plural = "멤버"
        ordering = ["id"]
