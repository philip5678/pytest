import pytest


def test_fixture01(product_fixture01):  # 当autouse=False时，要手动加上用fixture
    print("fixture 01  --------- " + str(product_fixture01))
    # assert 1 == 1


def test_fixture02(product02_alias, product_fixture01):  # 当autouse=False时，要手动加上用fixture
    print("fixture 02 --------- " + str(product_fixture01) + str(product02_alias))
    # assert 1 == 1


if __name__ == '__main__':
    pytest.main(['test_product.py'])
