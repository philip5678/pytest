import pytest


def test_fixture01(my_fixture01):  # 当autouse=False时，要手动加上用fixture
    print("fixture 01 前置 --------- " + str(my_fixture01))
    # assert 1 == 1


def test_fixture02(fixture_alias, my_fixture01):  # 当autouse=False时，要手动加上用fixture
    print("fixture 02 前置 --------- " + str(my_fixture01) + str(fixture_alias))
    # assert 1 == 1


if __name__ == '__main__':
    pytest.main(['test_fixture.py'])
