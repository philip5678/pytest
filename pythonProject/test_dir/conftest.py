import pytest


@pytest.fixture(scope="function", params=['中国', '加拿大', '美国'], ids="", name="")
def my_fixture01():
    print("前置 01 fixture practice")
    yield "success"  # 如果是空就是none
    # yield  # 如果是空就是none
    print("后置 01 fixture practice")


@pytest.fixture(scope="function", params=[' - 中国队', ' - 加拿大队', ' - 美国队'], ids=["China", "Canada", "USA"],
                name="fixture_alias")
def my_fixture02(request):
    print("前置 02 fixture practice")
    yield request.param
    print("后置 02 fixture practice")
