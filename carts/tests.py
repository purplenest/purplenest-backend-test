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
        pass

    def test_create(self):
        pass

    def test_update(self):
        pass

    def test_destroy(self):
        pass
