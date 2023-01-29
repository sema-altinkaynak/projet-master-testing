from src.exceptions.ParenthesisMissingException import ParenthesisMissingException
from src.exceptions.InputNotValidException import InputNotValidException
from src.calculator.Utilities import Utilities


class FakeScanner:

    def __init__(self) -> None:
        self.utility_helper = Utilities()

    def scan(self, input):
        input = input.strip()
        self.validate_input(input)

        tokens = input.split(' ')
        scanned_tokens = [self.convert_token(t) for t in tokens]
        return scanned_tokens

    def convert_token(self, token):
        if self.utility_helper.is_number(token):
            return float(token)
        return token

    def validate_input(self, input_as_string):
        self.validate_number_of_parenthesis_is_congruent(input_as_string)
        self.validate_last_character(input_as_string[-1])
        self.validate_first_character(input_as_string[0])

        tokens = input_as_string.split(' ')
        self.validate_there_is_at_least_one_operator(tokens)

        parenthesis_opened = 0

        for index in range(len(tokens) - 1):
            if  self.utility_helper.is_opening_parenthesis(tokens[index]):
                parenthesis_opened = parenthesis_opened + 1
            if self.utility_helper.is_closing_parenthesis(tokens[index]):
                parenthesis_opened = parenthesis_opened - 1

            if tokens[index].isnumeric():
                if parenthesis_opened == 0 and not self.utility_helper.is_operator(tokens[index + 1]):
                    raise InputNotValidException
                if parenthesis_opened > 0 and not (self.utility_helper.is_operator(tokens[index + 1]) or tokens[index + 1] == ')'):
                    raise InputNotValidException

        return True

    def validate_number_of_parenthesis_is_congruent(self, input):
        number_of_opening_parenthesis = input.count('(')
        number_of_closing_parenthesis = input.count(')')
        if number_of_opening_parenthesis == number_of_closing_parenthesis:
            return True
        else:
            raise ParenthesisMissingException

    def validate_first_character(self, character):
        if character.isnumeric() or self.utility_helper.is_opening_parenthesis(character) or character == '-':
            return True
        else:
            raise InputNotValidException

    def validate_last_character(self, character):
        if character.isnumeric() or self.utility_helper.is_closing_parenthesis(character):
            return True
        else:
            raise InputNotValidException

    def validate_there_is_at_least_one_operator(self, substrings):
        status = False
        for substring in substrings:
            if self.utility_helper.is_operator(substring):
                status = True
        if status:
            return status
        else:
            raise InputNotValidException
