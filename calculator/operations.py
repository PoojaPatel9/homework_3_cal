class Operations:
    """Static methods for basic arithmetic operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Adds two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtracts second number from first."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiplies two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divides first number by second, raises exception if dividing by zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
