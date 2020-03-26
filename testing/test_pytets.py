from python.calc import Calc
from math import fabs
import math
import pytest
import pytest_ordering

'''
等价类设计测试用例
--> 两数相加
1. 正数   1+99
2. 负数  -1 + （-99）
3. 正数+负数   99  +（-99）
4. 正数+0      10 + 0
5. 负数+0      -10 + 0
6  π + 任意数   π + 9.7

'''


class TestCalc:

    def setup_module(self):
        print("setup_module")

    @classmethod
    def setup_class(self):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def test_add(self):
        calc = Calc()
        assert calc.add(1, 2) == 3

    def test_add_1(self):
        calc = Calc()
        assert calc.add(1, 99) == 100

    def test_add_2(self):
        calc = Calc()
        assert calc.add(-1, -99) == -100

    def test_add_3(self):
        calc = Calc()
        assert calc.add(99, -99) == 0

    def test_add_4(self):
        calc = Calc()
        assert calc.add(8, 0) == 8

    @pytest.mark.run(order=-1)
    def test_add_5(self):
        calc = Calc()
        assert calc.add(-9, 0) == -9

    def test_add_6(self):
        calc = Calc()
        assert calc.add(math.pi, 9.7) == 12.84159265

    # --> 两数相除
    # 1. 正数(可整除)        99 / 3
    # 2. 负数（可整除）       -80 /  -5
    # 3. 被除数为0，除数为非0数    0  / (-8)
    # 4. 正数(不能整除)        98 / 3
    # 5. 负数（不能整除）      -79 / 3
    #
    # 无效等价类
    # 1. 被除数为任意数，除数是0   10 / 0
    @pytest.mark.run(order=1)
    def test_div_1(self):
        calc = Calc()
        assert calc.div(99, 3) == 33

    def test_div_2(self):
        calc = Calc()
        assert calc.div(-80, (-5)) == 16

    def test_div_3(self):
        calc = Calc()
        assert calc.div(0, (-8)) == 0

    def test_div_4(self):
        calc = Calc()
        assert calc.div(98, 3) == 32.67

    def test_div_5(self):
        calc = Calc()
        assert calc.div(-79, 3) == -26.33

    def test_div_6(self):
        calc = Calc()
        assert calc.div(10, 0) == 0


class Demo:
    kind = 0

    def __init__(self):
        self.name = ""


class TestCalc2:
    @classmethod
    def setup_class(self):
        print("setup_class \n")

    def test_Demo1(self):
        demo1 = Demo()
        demo2 = Demo()
        print(demo1.kind)
        print(demo2.kind)
        print(Demo.kind)

        Demo.kind = 1
        print(demo1.kind)
        print(demo2.kind)
        print(Demo.kind)

        demo1.kind = 2
        print(demo1.kind)
        print(demo2.kind)
        print(Demo.kind)

        demo2.kind = 3
        print(demo1.kind)
        print(demo2.kind)
        print(Demo.kind)
