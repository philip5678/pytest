import pytest


def test_fixture01(manager_fixture01, user_fixture01):  # , product_fixture01):  # 当autouse=False时，要手动加上用fixture
    print("fixture 01  --------- " + str(user_fixture01))
    # print("fixture 01  --------- " + str(product_fixture01))
    print("fixture 01  --------- " + str(manager_fixture01))
    # assert 1 == 1


def test_user02(user02_alias, user_fixture01):  # 当autouse=False时，要手动加上用fixture
    print("fixture 02 --------- " + str(user_fixture01) + str(user02_alias))
    # assert 1 == 1


if __name__ == '__main__':
    pytest.main(['test_user.py'])
