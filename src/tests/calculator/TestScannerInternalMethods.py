from src.calculator.FakeScanner import FakeScanner
from src.exceptions.InputNotValidException import InputNotValidException
from src.exceptions.ParenthesisMissingException import ParenthesisMissingException

import unittest


class TestScannerInternalMethods(unittest.TestCase):

    def setUp(self):
        self.scanner = FakeScanner()

    def test_check_number_of_parenthesis_is_congruent(self):
        self.assertTrue(
            self.scanner.validate_number_of_parenthesis_is_congruent('((()))())(()'))

    def test_check_number_of_parenthesis_is_not_congruent(self):
        with self.assertRaises(ParenthesisMissingException):
            self.scanner.validate_number_of_parenthesis_is_congruent(
                '((())())(()')

    def test_check_number_of_parenthesis_is_congruent_in_expression(self):
        self.assertTrue(self.scanner.validate_number_of_parenthesis_is_congruent(
            '(5 + (6 * 8) / 6) + 66'))

    def test_check_number_of_parenthesis_is_not_congruent_in_expression(self):
        with self.assertRaises(ParenthesisMissingException):
            self.scanner.validate_number_of_parenthesis_is_congruent(
                '(5 + 6 * 8) / 6) + 66')

    # validate_first_character
    def test_check_first_character_is_valid_numbers(self):
        self.assertTrue(self.scanner.validate_first_character('4'))
        self.assertTrue(self.scanner.validate_first_character('444'))
        self.assertTrue(self.scanner.validate_first_character('044'))
        input = '4444'
        self.assertTrue(self.scanner.validate_first_character(input[0]))

    def test_check_first_character_is_valid_perenthesis(self):
        self.assertTrue(self.scanner.validate_first_character('('))

    def test_check_first_character_not_is_valid(self):
        with self.assertRaises(InputNotValidException):
            self.scanner.validate_first_character('+')
            self.scanner.validate_first_character('-')
            self.scanner.validate_first_character('/')
            self.scanner.validate_first_character('.')
            self.scanner.validate_first_character(')')

    # validate_last_character
    def test_validate_last_character(self):
        self.assertTrue(self.scanner.validate_last_character(')'))
        self.assertTrue(self.scanner.validate_last_character('444'))
        self.assertTrue(self.scanner.validate_last_character('3'))
        input = '4444'
        self.assertTrue(self.scanner.validate_last_character(input[-1]))

    def test_validate_last_character_is_not_valid(self):
        with self.assertRaises(InputNotValidException):
            self.scanner.validate_first_character('+')
            self.scanner.validate_first_character('-')
            self.scanner.validate_first_character('/')
            self.scanner.validate_first_character('.')
            self.scanner.validate_first_character('(')
            input = '4444('
            self.assertTrue(self.scanner.validate_last_character(input[-1]))


if __name__ == '__main__':
    unittest.main()
