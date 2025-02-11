from typing import List
from calculator.calculation import Calculation

class Calculations:
    """Manages the history of calculations."""
    
    history: List[Calculation] = []

    @classmethod
    def add_to_history(cls, calc: Calculation):
        """Adds a calculation to the history."""
        cls.history.append(calc)

    @classmethod
    def view_history(cls):
        """Displays the history of calculations."""
        if cls.history:
            print("History of Calculations:")
            for index, calc in enumerate(cls.history):
                print(f"{index+1}. {calc.a} {calc.operation.__name__} {calc.b} = {calc.result}")
        else:
            print("No history available.")
