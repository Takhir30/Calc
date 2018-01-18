import pytest,calc_1

def test_result():
    assert calc_1.calc('2*3/2*100') == 300.0

def test_result_1():
    assert calc_1.calc('2*3/6-7') == -6.0

def test_result_2():
    assert calc_1.calc('12/6-2*9/3') == -4.0
