from model_bakery import baker
from rest_framework.test import APITestCase

from users.models import User


class OrderAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = baker.make(User)

    def setUp(self) -> None:
        self.client.force_authenticate(self.user)

    def test_list(self):
        """주문 목록"""
        pass

    def test_create_from_cart(self):
        """장바구니에 있는 항목들로 Order생성"""
        pass

    def test_create_direct(self):
        """장바구니를 거치지않고 product와 qty를 사용해 곧바로 Order생성"""
        pass

    def test_destroy(self):
        """삭제"""
        pass


class OrderItemAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = baker.make(User)

    def setUp(self) -> None:
        self.client.force_authenticate(self.user)

    def test_create(self):
        """이미 존재하는 Order에 항목 추가"""
        pass

    def test_update(self):
        """수량변경"""
        pass

    def test_destroy(self):
        """삭제"""
        pass
