import pytest


@pytest.fixture
def conn_db():
    print("执行setup")
    yield "fixture返回值"
    print("执行teardown")


#装饰器参数化，request是固定写法
@pytest.fixture(params=[1,2,2])
def login(request):
    print("执行setup")
    yield f"fixture返回值{request.param}"
    print("执行teardown")
