import pytest

from testing.calculator import Calculator


class TestClac:
    def setup(self):
        print("计算开始")
        self.calc = Calculator()

    @pytest.mark.parametrize('num1,num2,res',[(1,1,2),(100,100,200),(0.1,0.01,0.11)],ids=['case1','case2','case3'])
    def test_add(self,num1,num2,res):
        result = self.calc.add(num1,num2)
        assert result == res

    @pytest.mark.parametrize('num1,num2,res', [(1, 0, 2), (100, 2, 200)])
    def test_div(self, num1, num2, res):
        try:
            self.calc.div(num1, num2)
        except Exception :
            print("请输入非0分母")

    @pytest.mark.parametrize('num1,num2,res', [(1, 0, 2), (100, 2, 200)])
    def test_mul(self, num1, num2, res):
        result = self.calc.mul(num1, num2)
        assert res == result

    # def test_add1(self):
    #     result = self.calc.add(100, 100)
    #     assert result == 200
    #
    # def test_add2(self):
    #     result = self.calc.add(0.1, 0.01)
    #     assert result == 0.11