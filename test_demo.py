import allure
import pytest
import yaml


def func(num):
    return num+2;
@pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
def test_answer(a,b):
    assert  func(a) == b

def test_answer1():
    assert  func(4) == 5


@pytest.fixture()
def fixdemo():
    print("登陆")
    yield "username=jerry"
    print("teardown")
    #return "username=jerry"

@allure.feature("这里是测试模块")
class TestClass:
    @allure.story("这里是第一个case")
    def test_a(self,fixdemo):
        print(f"a   {fixdemo}")

    @allure.story("这里是第二个case")
    @pytest.mark.parametrize("a",[1,2])
    @pytest.mark.parametrize("b",[9,])
    #使用装饰器方式调用fixture 无内容承接yield返回值
    @pytest.mark.usefixtures("fixdemo")
    def test_b(self,a,b):
        print(f"{a}+{b}={a+b}       ,{fixdemo}")
if __name__ == '__main__':
    pytest.main(['test_demo.py::test_answer','-v'])

def test_direct():
    a = {"name":"nihao"}
    print(type(a))