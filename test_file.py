import pytest,calc_3

def test_result():
    assert calc_3.calc('2*3/2*100') == '300.00'

def test_div_by_zero():
    assert calc_3.calc('2/0') == "ZeroDivisionError!!! Try again!"

def test_div_by_zero_part():
    if calc_3.calc ('2/0'):
        assert calc_3.div(['2','/','0']) == calc_3.calc("ZeroDivisionError")
