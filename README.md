# 퍼플네스트 백엔드 코딩테스트 프로젝트

퍼플네스트의 백엔드 코딩테스트를 위한 프로젝트입니다.

## 설치

가상환경 설정 후, 패키지를 설치합니다.

```shell
pip install -r requirements.txt
```

## 테스트코드 실행

```shell
purplestore ❯ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....FFF......
======================================================================
FAIL: test_order_orm (config.tests.ORMTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/lhy/projects/purplestore-test-backend-project/config/tests.py", line 53, in test_order_orm
    self.assertEqual(order.total_price, total_price)
AssertionError: '' != 5100

======================================================================
FAIL: test_product_orm (config.tests.ORMTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/lhy/projects/purplestore-test-backend-project/config/tests.py", line 58, in test_product_orm
    self.assertEqual(
AssertionError: '' != 3

======================================================================
FAIL: test_user_orm (config.tests.ORMTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/lhy/projects/purplestore-test-backend-project/config/tests.py", line 72, in test_user_orm
    self.assertEqual(user1.total_order_price, 69450)
AssertionError: '' != 69450

----------------------------------------------------------------------
Ran 13 tests in 0.095s

FAILED (failures=3)
Destroying test database for alias 'default'...
```

