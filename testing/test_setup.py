


def test_case1():
    print("case1")


def setup_function():
    print("资源准备：setuo function")

def teardown_function():
    print(("资源销毁：teardown funcion"))


class TestDemo():

    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("setup_class")

    def setup(self):
        print("setup")

    def teardown(self):
        print("setup")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")