import pytest
import calc_1


def test_result():
    assert calc_1.check('2*3/2*100') == 300.00


def test_result_1():
    assert calc_1.check('2*3/6-7') == -6.00


def test_result_2():
    assert calc_1.check('12/6-2*9/3') == -4.00


def test_result_parenthesis():
    assert calc_1.check('12/(6-2)*9/3') == 9.00


def test_result_negative():
    assert calc_1.check('(-1)/(-1)') == 1.00


def test_result_trigonometry():
    assert calc_1.check('12/(6-2)*9/3/sin30') == 18.00


def test_result_wrong_symbol():
    assert calc_1.check('1+2+3gv') == 'Wrong input!!! You may use only 1 2 3 4 5 6 7 8 9 0 . ( ) + - * / cos sin symbols! Try again!'
