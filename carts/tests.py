from model_bakery import baker
from rest_framework.test import APITestCase

from users.models import User


class CartItemAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = baker.make(User)

    def setUp(self) -> None:
        self.client.force_authenticate(self.user)

    def test_list(self):
        """장바구니에 담은 목록"""
        pass

    def test_create(self):
        """장바구니 항목 추가"""
        pass

    def test_update(self):
        """수량 업데이트"""
        pass

    def test_destroy(self):
        """삭제"""
        pass
