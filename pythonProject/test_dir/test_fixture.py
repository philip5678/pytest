import pytest


@pytest.fixture(scope="function", params=['中国', '加拿大', '美国'], ids="", name="")
def my_fixture01():
    print("前置 01 fixture practice")
    yield "success"  # 如果是空就是none
    # yield   #如果是空就是none
    print("后置 01 fixture practice")


def test_fixture01(my_fixture01):  # 当autouse=False时，要手动加上用fixture
    print("fixture 01 前置 --------- " + str(my_fixture01))
    # assert 1 == 1


@pytest.fixture(scope="function", params=['中国', '加拿大', '美国'], ids=["China", "Canada", "USA"], name="fixture_alias")
def my_fixture02(request):
    print("前置 02 fixture practice")
    yield request.param
    print("后置 02 fixture practice")


def test_fixture02(fixture_alias):  # 当autouse=False时，要手动加上用fixture
    print("fixture 02 前置 --------- " + str(fixture_alias))
    # assert 1 == 1


if __name__ == '__main__':
    pytest.main(['test_fixture.py'])
