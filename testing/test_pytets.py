from python.calc import Calc


class TestCalc:
    def test_add(self):
        calc = Calc()
        assert calc.add(1, 2) == 3

    def test_div(self):
        calc = Calc()
        assert calc.div(1, 2) == 0.5
