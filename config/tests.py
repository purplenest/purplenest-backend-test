from itertools import cycle

from django.test import TestCase
from model_bakery import baker

from orders.models import Order, OrderItem
from products.models import Product
from users.models import User


class ORMTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1, cls.user2, cls.user3 = user1, user2, user3 = baker.make(User, _quantity=3)
        user1_orders = baker.make(Order, user=user1, _quantity=3)
        user2_orders = baker.make(Order, user=user2, _quantity=6)
        user3_orders = baker.make(Order, user=user3, _quantity=20)

        products = baker.make(Product, price=cycle([i * 150 for i in range(1, 10)]), _quantity=9)

        # product[0~2]로 users[0]의 Order에 OrderItem생성
        baker.make(
            OrderItem,
            product=cycle(products[:3]),
            order=cycle(user1_orders),
            qty=cycle([1, 2, 3]),
            _quantity=100,
        )
        # product[0~6]로 users[1]의 Order에 OrderItem생성
        baker.make(
            OrderItem,
            product=cycle(products[:6]),
            order=cycle(user2_orders),
            qty=cycle([1, 2, 3]),
            _quantity=100,
        )
        # product[0~9]로 users[2]의 Order에 OrderItem생성
        baker.make(
            OrderItem,
            product=cycle(products),
            order=cycle(user3_orders),
            qty=cycle([1, 2, 3]),
            _quantity=100,
        )

    def test_order_orm(self):
        # Order.total_price확인
        for order in Order.objects.annotate_total_price():
            # Order에 속한 OrderItem들의 가격 * 수량의 합
            total_price = 0
            for order_item in order.item_set.all():
                total_price += order_item.product.price * order_item.qty
            self.assertEqual(order.total_price, total_price)

    def test_product_orm(self):
        # Product.ordered_user_count확인
        for product in Product.objects.annotate_ordered_user_count():
            self.assertEqual(
                product.ordered_user_count,
                User.objects.filter(order__item__product=product).distinct().count(),
            )

    def test_user_orm(self):
        # User의 annotate된
        #  total_order_price
        #  avg_order_price
        #  total_grade
        #  avg_grade
        # 값들을 확인
        users = User.objects.annotate_grade().order_by("id")
        user1 = users.get(id=self.user1.id)
        self.assertEqual(user1.total_order_price, 69450)
        self.assertEqual(user1.avg_order_price, 23150)

        user2 = users.get(id=self.user2.id)
        self.assertEqual(user2.total_order_price, 113100)
        self.assertEqual(user2.avg_order_price, 18850)

        user3 = users.get(id=self.user3.id)
        self.assertEqual(user3.total_order_price, 158550)
        self.assertEqual(user3.avg_order_price, 7927)

        for user in User.objects.annotate_grade().order_by("id"):
            total_price = 0
            for order in Order.objects.filter(user=user).prefetch_related("item_set__product"):
                for item in order.item_set.all():
                    total_price += item.product.price * item.qty

            self.assertEqual(user.total_order_price, total_price)
            self.assertEqual(user.avg_order_price, total_price // user.order_set.count())

        for user, total_grade, avg_grade in zip(
            User.objects.annotate_grade().order_by("id"),
            ["일반회원", "열심회원", "우수회원"],
            ["퍼스트", "비즈니스", "일반"],
        ):
            self.assertEqual(user.total_grade, total_grade)
            self.assertEqual(user.avg_grade, avg_grade)
