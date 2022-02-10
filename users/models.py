from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db.models import Value

from orders.models import Order, OrderItem


class UserManager(BaseUserManager):
    def annotate_grade(self):
        """
        User와 연결된 Order정보를 annotate
         total_order_price: User의 모든 Order가격 합
         avg_order_price: User의 Order가격 평균
         total_grade:
            User의 모든 Order가격 합이
             15만원 이상인 경우 -> "우수회원"
             10만원 이상인 경우 -> "열심회원"
             그 외 -> "일반회원"
         avg_grade:
            User의 Order가격 평균이
             20000원 이상인 경우 -> "퍼스트"
             10000원 이상인 경우 -> "비즈니스"
             그 외 -> "일반"
        :return: QuerySet
        """
        return self.annotate(
            # User의 모든 Order가격 합
            total_order_price=Value(""),
            # User의 Order가격 평균
            #  ex) 3개의 Order가 각각 가격합이 5000, 10000, 30000인 경우 -> 15000
            avg_order_price=Value(""),
            # User의 모든 Order가격 합이
            #  15만원 이상인 경우 -> "우수회원"
            #  10만원 이상인 경우 -> "열심회원"
            #  그 외 -> "일반회원"
            total_grade=Value(""),
            # User의 Order가격 평균이
            #  20000원 이상인 경우 -> "퍼스트"
            #  10000원 이상인 경우 -> "비즈니스"
            #  그 외 -> "일반"
            avg_grade=Value(""),
        )


class User(AbstractUser):
    objects = UserManager()
