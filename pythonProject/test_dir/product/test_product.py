import pytest


def test_fixture01(product_fixture01):  # 当autouse=False时，要手动加上用fixture
    print("fixture 01  --------- " + product_fixture01)
    print(f'{type(product_fixture01)=}')
    assert product_fixture01 == "success"


def test_fixture02(product02_alias, product_fixture01):  # 当autouse=False时，要手动加上用fixture
    print("fixture 02 --------- " + product_fixture01 + product02_alias)
    # assert 1 == 1
    assert product_fixture01 == "success"


if __name__ == '__main__':
    pytest.main(['test_product.py'])
