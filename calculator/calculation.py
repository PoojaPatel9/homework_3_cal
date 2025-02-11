from calculator.operations import Operations

class Calculation:
    """Represents a single calculation."""
    
    def __init__(self, a: float, b: float, operation):
        self.a = a
        self.b = b
        self.operation = operation
        self.result = self.perform_calculation()

    def perform_calculation(self) -> float:
        return self.operation(self.a, self.b)
