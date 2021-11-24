from django.db import models
from server.base.models import BaseModel


def image_upload_to(instance, filename):
    return os.path.join(instance.UPLOAD_PATH, f"{filename}")


class ShoppingMall(BaseModel):
    UPLOAD_PATH = "shoppingmall"

    image = models.ImageField(
        upload_to=image_upload_to,
        verbose_name="쇼핑몰 의류 이미지",
    )
    brand = models.ForeignKey(
        "common.Brand", null=True, verbose_name="브랜드", on_delete=models.CASCADE
    )
    cloth = models.ManyToManyField(
        "cloth.Clothes",
        verbose_name="의류",
    )
    url = models.TextField(verbose_name="웹 페이지 URL")
    price = models.CharField("가격",max_length=64, default=0)

    def __str__(self):
        return f"쇼핑몰({self.id})"

    class Meta:
        db_table = "shoppingmall_shoppingmall"
        verbose_name = "쇼핑몰"
        verbose_name_plural = "쇼핑몰"
        ordering = ["id"]
