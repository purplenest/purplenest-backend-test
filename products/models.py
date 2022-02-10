from django.db import models
from django.db.models import Value

from users.models import User


class ProductManager(models.Manager):
    def annotate_ordered_user_count(self):
        """
        이 상품을 주문한 유저 수를 orderd_user_count속성으로 annotate
        :return: QuerySet
        """
        return self.annotate(
            ordered_user_count=Value(""),
        )


class Product(models.Model):
    name = models.CharField("상품명", max_length=100)
    price = models.PositiveIntegerField("가격")
    objects = ProductManager()
