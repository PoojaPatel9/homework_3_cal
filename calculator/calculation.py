class Calculation:
    """Class to store a single calculation instance."""
    
    def __init__(self, operation: str, a: float, b: float, result: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result

    def __str__(self):
        return f"{self.a} {self.operation} {self.b} = {self.result}"
