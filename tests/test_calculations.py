import pytest
from calculator.calculation import Calculation
from calculator.operations import Operations
from calculator.calculations import Calculations

@pytest.fixture
def calc_addition():
    """Fixture for addition operation."""
    return Calculation(7, 5, Operations.add)

@pytest.fixture
def calc_division():
    """Fixture for division operation."""
    return Calculation(16, 4, Operations.divide)

@pytest.mark.parametrize("a, b, expected_result", [
    (5, 3, 8),
    (10, -5, 5),
    (0, 5, 5)
])
def test_addition(a, b, expected_result):
    """Test the addition operation."""
    calc = Calculation(a, b, Operations.add)
    assert calc.result == expected_result
""""
@pytest.mark.parametrize("a, b, expected_result", [
    (10, 2, 5),
    (6, 3, 2),
    (10, -2, -5)
])"""
def test_division(a, b, expected_result):
    """Test the division operation."""
    calc = Calculation(a, b, Operations.divide)
    assert calc.result == expected_result

def test_history():
    """Test that the history is being tracked."""
    calc1 = Calculation(5, 3, Operations.add)
    calc2 = Calculation(10, 2, Operations.subtract)
    Calculations.add_to_history(calc1)
    Calculations.add_to_history(calc2)
    assert len(Calculations.history) == 2
    assert Calculations.history[0].result == 8
    assert Calculations.history[1].result == 8
