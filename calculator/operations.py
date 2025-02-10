from typing import List

class Calculator:
    history: List[str] = []  # store history

    def __init__(self):
        self.clear_history()

    @classmethod
    def clear_history(cls):
        """Class method to clear the history of calculations."""
        cls.history.clear()

    def add(self, a: float, b: float) -> float:
        """Adds two numbers and records the operation."""
        result = a + b
        self._add_to_history(f"Added: {a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtracts b from a and records the operation."""
        result = a - b
        self._add_to_history(f"Subtracted: {a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiplies two numbers and records the operation."""
        result = a * b
        self._add_to_history(f"Multiplied: {a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divides a by b, throws exception if dividing by zero, and records the operation."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        self._add_to_history(f"Divided: {a} / {b} = {result}")
        return result

    def _add_to_history(self, operation: str):
        """Add a calculation to the history."""
        Calculator.history.append(operation)

    def retrieve_history(self) -> List[str]:
        """Returns the history of calculations."""
        return Calculator.history
