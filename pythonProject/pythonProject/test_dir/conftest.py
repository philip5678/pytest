import pytest


@pytest.fixture(scope="function", params=['中国', '加拿大', '美国'], ids=["-China1", "-Canada1", "-USA1"], name="")
def manager_fixture01():
    print("\nmanager 前置 01 fixture practice")
    yield "success"  # 如果是空就是none
    # yield  # 如果是空就是none
    print("\nmanager 后置 01 fixture practice")


@pytest.fixture(scope="function", params=[' - 中国队', ' - 加拿大队', ' - 美国队'], ids=["China2", "Canada2", "USA2"],
                name="manager02_alias")
def manager_fixture02(request): #params,request,request.param都是固定写法
    print("\nmanager 前置 02 fixture practice")
    yield request.param
    print("\nmanager 后置 02 fixture practice")
