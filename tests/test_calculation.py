""" 
Test suite for the Calculator class and its operations.

contains tests to ensure the correct functionality of the 
Calculator class, including basic arithmetic operations and error handling.
"""
import pytest
from calculator.operations import Calculator

@pytest.fixture
def calc():
    """Initialize the Calculator class."""
    calculator = Calculator()
    calculator.clear_history()  # Clear history before each test
    return calculator

@staticmethod
def test_add(calc: Calculator):
    """Test add function of the Calculator class."""
    result = calc.add(1, 2)
    assert result == 3
    assert len(calc.retrieve_history()) == 1

def test_subtract(calc: Calculator):
    """Test subtract function of the Calculator class."""
    result = calc.subtract(5, 3)
    assert result == 2
    assert len(calc.retrieve_history()) == 1

def test_multiply(calc: Calculator):
    """Test multiply function of the Calculator class."""
    result = calc.multiply(2, 3)
    assert result == 6
    assert len(calc.retrieve_history()) == 1

def test_divide(calc: Calculator):
    """Test divide function of the Calculator class."""
    result = calc.divide(6, 3)
    assert result == 2
    assert len(calc.retrieve_history()) == 1

def test_divide_by_zero(calc: Calculator):
    """Test division by zero in the Calculator class."""
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)

def test_retrieve_history(calc: Calculator):
    """Test retrieving history from the Calculator class."""
    calc.add(2, 3)
    history = calc.retrieve_history()
    assert len(history) == 1
    assert history[0] == "Added: 2 + 3 = 5"
