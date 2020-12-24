import pytest


@pytest.fixture(scope="function", params=['中国', '加拿大', '美国'], ids=["-China1", "-Canada1", "-USA1"], name="")
def product_fixture01():
    print("\nproduct 前置 01 fixture practice")
    yield "success"  # 如果是空就是none
    # yield  # 如果是空就是none
    print("\nproduct 后置 01 fixture practice")


@pytest.fixture(scope="function", params=[' - 中国队', ' - 加拿大队', ' - 美国队'], ids=["China2", "Canada2", "USA2"],
                name="product02_alias")
def product_fixture02(request):
    print("\nproduct 前置 02 fixture practice")
    yield request.param
    print("\nproduct 后置 02 fixture practice")
