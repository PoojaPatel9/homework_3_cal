import pytest
from main import calculate_and_print  # Ensure this import matches your project structure

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8.0"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8.0"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20.0"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5.0"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Adjusted for the actual error message
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")  # Testing another invalid number input
])

def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    # Call the function under test
    calculate_and_print(a_string, b_string, operation_string)
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert that the captured output matches the expected string
    assert captured.out.strip() == expected_string

def test_operations(a, b, operation, expected):
    # Call the main calculation function
    calculate_and_print(a, b, operation)
    # You can optionally add further checks here for logging or other outputs

# Test cases to ensure 100% coverage
def test_invalid_input(capsys):
    # Test invalid number input
    calculate_and_print("abc", "123", "add")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Invalid number input: abc or 123 is not a valid number."

def test_zero_division(capsys):
    # Test divide by zero case
    calculate_and_print("10", "0", "divide")
    captured = capsys.readouterr()
    assert captured.out.strip() == "An error occurred: Cannot divide by zero"

def test_unknown_operation(capsys):
    # Test for an unknown operation
    calculate_and_print("5", "3", "modulo")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Unknown operation: modulo"
    