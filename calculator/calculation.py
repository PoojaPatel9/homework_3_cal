from calculator.operations import Operations

class Calculation:
    """Represents a single calculation."""

    def __init__(self, a: float, b: float, operation):
        """Initialize calculation with two numbers and an operation function."""
        self.a = a
        self.b = b
        self.operation = operation
        self.result = self.perform_calculation()

    def perform_calculation(self) -> float:
        """Executes the stored operation."""
        return self.operation(self.a, self.b)
