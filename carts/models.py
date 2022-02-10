from django.db import models


class CartItem(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField("수량")
