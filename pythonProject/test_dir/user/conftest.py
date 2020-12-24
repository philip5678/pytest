import pytest


@pytest.fixture(scope="function", params=['中国', '加拿大', '美国'], ids=["-China1", "-Canada1", "-USA1"], name="")
def user_fixture01():
    print("\nuser 前置 01 fixture practice")
    yield "success"  # 如果是空就是none
    # yield  # 如果是空就是none
    print("\nuser  后置 01 fixture practice")


@pytest.fixture(scope="function", params=[' - 中国队', ' - 加拿大队', ' - 美国队'], ids=["China2", "Canada2", "USA2"],
                name="user02_alias")
def user_fixture02(request):
    print("\nuser  前置 02 fixture practice")
    yield request.param
    print("\nuser  后置 02 fixture practice")
