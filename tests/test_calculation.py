# pylint: disable=unnecessary-dunder-call, invalid-name


"""Test cases for the Calculation class, testing different arithmetic operations."""


import pytest

from calculator.calculation import Calculation
from calculator.operations import Operations


def test_addition():
    """Test the addition operation of the Calculation class."""
    calc = Calculation(3, 2, Operations.add)
    assert calc.result == 5

def test_subtraction():
    """Test the subtraction operation of the Calculation class."""
    calc = Calculation(5, 3, Operations.subtract)
    assert calc.result == 2

def test_multiplication():
    """Test the multiplication operation of the Calculation class."""
    calc = Calculation(4, 3, Operations.multiply)
    assert calc.result == 12

def test_division():
    """Test the division operation of the Calculation class."""
    calc = Calculation(10, 2, Operations.divide)
    assert calc.result == 5

def test_division_by_zero():
    """Test division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Calculation(10, 0, Operations.divide)
        # At the very end of the file, add an empty line.
