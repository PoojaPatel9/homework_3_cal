# pylint: disable=unnecessary-dunder-call, invalid-name
"""
Tests for the Calculations class.
This module contains unit tests to validate the functionality
of the Calculations class and its methods.
"""
import pytest
from calculator.operations import Operations
from calculator.calculation import Calculation
from calculator.calculations import Calculations

def test_addition():
    """Test the addition operation."""
    Calculations.history = []
    calc = Calculation(1, 2, Operations.add)
    assert calc.result == 3
    Calculations.add_to_history(calc)
    assert len(Calculations.history) == 1
    assert Calculations.history[0] == calc

def test_subtraction():
    """Test the subtraction operation."""
    Calculations.history = []
    calc = Calculation(5, 2, Operations.subtract)
    assert calc.result == 3
    Calculations.add_to_history(calc)
    assert len(Calculations.history) == 1
    assert Calculations.history[0] == calc

def test_multiplication():
    """Test the multiplication operation and verify that it is added to history."""
    Calculations.history = []
    calc = Calculation(4, 3, Operations.multiply)
    assert calc.result == 12
    Calculations.add_to_history(calc)
    assert len(Calculations.history) == 1
    assert Calculations.history[0] == calc

def test_division():
    """Test the division operation and verify that it is added to history."""
    Calculations.history = []
    calc = Calculation(10, 2, Operations.divide)
    assert calc.result == 5
    Calculations.add_to_history(calc)
    assert len(Calculations.history) == 1
    assert Calculations.history[0] == calc

def test_division_by_zero():
    """Test division by zero and ensure it raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Calculation(10, 0, Operations.divide)

def test_history(capsys):
    """Test the calculation history functionality."""
    Calculations.history = []
    calc1 = Calculation(3, 2, Operations.add)
    calc2 = Calculation(5, 3, Operations.subtract)
    Calculations.add_to_history(calc1)
    Calculations.add_to_history(calc2)
    assert len(Calculations.history) == 2
    assert Calculations.history[0] == calc1
    assert Calculations.history[1] == calc2
    # Capture the output of the view_history method
    Calculations.view_history()
    # Capture the standard output and compare it
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')[1:]  # Skip the first line (header)
    assert len(output) == 2  # Ensure there are two history entries
    assert output[0] == "1. 3 add 2 = 5"
    assert output[1] == "2. 5 subtract 3 = 2"
