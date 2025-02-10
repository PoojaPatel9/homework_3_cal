import pytest
from calculator.calculation import Calculation
from calculator.operations import Operations

def test_addition():
    calc = Calculation(3, 2, Operations.add)
    assert calc.result == 5

def test_subtraction():
    calc = Calculation(5, 3, Operations.subtract)
    assert calc.result == 2

def test_multiplication():
    calc = Calculation(4, 3, Operations.multiply)
    assert calc.result == 12

def test_division():
    calc = Calculation(10, 2, Operations.divide)
    assert calc.result == 5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculation(10, 0, Operations.divide)
