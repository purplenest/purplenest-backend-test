from django.db import models
from django.db.models import Value


class OrderManager(models.Manager):
    def annotate_total_price(self):
        """
        주문의 금액합계를 total_price속성으로 annotate
        :return: QuerySet
        """
        return self.annotate(
            total_price=Value(""),
        )


class Order(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.PROTECT)
    objects = OrderManager()


class OrderItem(models.Model):
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE, related_name="item_set", related_query_name="item")
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT)
    qty = models.PositiveSmallIntegerField("수량")
