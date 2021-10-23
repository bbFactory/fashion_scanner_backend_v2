from django.db import models
from server.base.models import BaseModel


def image_upload_to(instance, filename):
    return os.path.join(instance.UPLOAD_PATH, f"{filename}")


class Clothes(BaseModel):
    UPLOAD_PATH = "clothes"

    image = models.ImageField(
        upload_to=image_upload_to,
        verbose_name="의류 이미지",
    )
    member = models.ForeignKey(
        "member.Members", null=True, verbose_name="멤버", on_delete=models.CASCADE
    )
    color = models.ForeignKey(
        "common.Color", null=True, verbose_name="의류 색상", on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        "cloth.Category", null=True, verbose_name="의류 카테고리", on_delete=models.CASCADE
    )
    attributes = models.ManyToManyField(
        "cloth.Attribute",
        verbose_name="의류 속성",
    )

    def __str__(self):
        return f"의류({self.id})"

    class Meta:
        db_table = "cloth_clothes"
        verbose_name = "의류"
        verbose_name_plural = "의류"
        ordering = ["id"]


class Category(models.Model):
    ko_name = models.CharField(max_length=32, verbose_name="의류 카테고리 한국어")
    en_name = models.CharField(max_length=32, verbose_name="의류 카테고리 영어")

    def __str__(self):
        return f"{self.en_name}({self.ko_name})"

    class Meta:
        db_table = "cloth_category"
        verbose_name = "의류 카테고리"
        verbose_name_plural = "의류 카테고리"
        ordering = ["id"]


class Attribute(models.Model):
    ko_name = models.CharField(max_length=32, verbose_name="의류 속성 한국어")
    en_name = models.CharField(max_length=32, unique=True, verbose_name="의류 속성 영어")

    def __str__(self):
        return f"{self.en_name}({self.ko_name})"

    class Meta:
        db_table = "cloth_attribute"
        verbose_name = "의류 속성"
        verbose_name_plural = "의류 속성"
        ordering = ["id"]
