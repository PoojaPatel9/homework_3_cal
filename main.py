import sys
from decimal import Decimal, InvalidOperation

from calculator.operations import Operations


def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Operations.add,
        'subtract': Operations.subtract,
        'multiply': Operations.multiply,
        'divide': Operations.divide
    }

    try:
        a_float, b_float = map(float, [a, b])
        result = operation_mappings.get(operation_name)  # Use get to handle unknown operations
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_float, b_float)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except ValueError:  # Handle invalid number input
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:  # Handle division by zero
        print("An error occurred: Cannot divide by zero")
    except Exception as e:  # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

if __name__ == '__main__':
    main()
