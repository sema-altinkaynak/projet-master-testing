from src.calculator.FakeParser import FakeParser
from src.calculator.FakeScanner import FakeScanner
from src.database.DbDao import DbDao


# We could also have a history instance variable.
# The calculator will have the responsibility of keeping the history.
# Like that, the calculator will have more responsabilities
# If we want to add an user interface, it needs to be in this class


class Calculator:

    def __init__(self) -> None:
        self.parser = FakeParser()
        self.scanner = FakeScanner()
        self.db = DbDao()
        # For the moment, we don't manage the history
        self.history = []
        

    def calculate(self, expression_as_string):
        scanned_input = self.scanner.scan(expression_as_string)
        calculation_result = self.parser.parse(scanned_input)
        self.db.addCalcul(expression_as_string, calculation_result)
        return calculation_result

