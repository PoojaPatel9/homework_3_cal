from calculator.calculation import Calculation


class Calculations:
    """Class to manage the history of calculations."""

    history = []

    @classmethod
    def add_to_history(cls, calc: Calculation):
        """Adds a calculation result to the history."""
        cls.history.append(calc)

    @classmethod
    def view_history(cls):
        """Displays all past calculations."""
        if not cls.history:
            print("No history available.")
            return
        for index, calc in enumerate(cls.history, start=1):
            print(f"Calculation {index}: {calc.a} {calc.operation.__name__} {calc.b} = {calc.result}")

    @classmethod
    def get_last_calculation(cls):
        """Returns the last calculation from history."""
        return cls.history[-1] if cls.history else None
