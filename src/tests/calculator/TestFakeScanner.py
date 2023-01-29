from src.exceptions.ParenthesisMissingException import ParenthesisMissingException
from src.exceptions.InputNotValidException import InputNotValidException
from src.calculator.FakeScanner import FakeScanner

import unittest


class TestFakeScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = FakeScanner()

    # Invalid operations
    def test_invalid_input_only_one_number(self):
        with self.assertRaises(InputNotValidException):
            self.scanner.scan('533')

    def test_invalid_input_without_operators(self):
        with self.assertRaises(InputNotValidException):
            self.scanner.scan('( 5 )')

    def test_invalid_input_without_operators_two(self):
        with self.assertRaises(InputNotValidException):
            self.scanner.scan('( 5 6 )')

    def test_invalid_input_only_without_operator(self):
        with self.assertRaises(InputNotValidException):
            self.scanner.scan('35 4')

    def test_parenthesis_missing_closing(self):
        with self.assertRaises(ParenthesisMissingException):
            self.scanner.scan('( 5 + 4')

    def test_parenthesis_missing_opening(self):
        with self.assertRaises(ParenthesisMissingException):
            self.scanner.scan('555 + 43 )')

    def test_invalid_input_without_operator_after_parenthesis(self):
        with self.assertRaises(InputNotValidException):
            self.scanner.scan('35 + 4 ( 4 / 7 )')

    def test_invalid_input_missing_spaces(self):
        with self.assertRaises(InputNotValidException):
            self.scanner.scan('35 + 4 (4 / 7 )')

    # Valid operations
    def test_valid_simple_operation(self):
        scanned_tokens = self.scanner.scan('5333 + 4 + 3535')
        expected_tokens = [5333, '+', 4, '+', 3535]
        self.assertListEqual(scanned_tokens, expected_tokens)

    def test_valid_operation_with_multiple_operators(self):
        scanned_tokens = self.scanner.scan('55 + 433 * 6 - 9 + 2 / 555')
        expected_tokens = [55, '+', 433, '*', 6, '-', 9, '+', 2, '/', 555]
        self.assertListEqual(scanned_tokens, expected_tokens)

    def test_valid_operation_with_parenthesis(self):
        scanned_tokens = self.scanner.scan('544 + ( ( 45 * 6 ) / 233 ) - 9')
        expected_tokens = [
            544, '+', '(', '(', 45, '*', 6, ')', '/', 233, ')', '-', 9]
        self.assertListEqual(scanned_tokens, expected_tokens)

    def test_valid_with_decimal_numbers_simple(self):
        scanned_tokens = self.scanner.scan('9.9 + 5.5')
        expected_tokens = [9.9, '+', 5.5]
        self.assertListEqual(scanned_tokens, expected_tokens)

    def test_valid_with_decimal_numbers_complex(self):
        scanned_tokens = self.scanner.scan(
            '9.9 + ( 5.5 / 0.008 ) * ( 5 * ( 4 / 9.7 ) ) - 9.99')
        expected_tokens = [9.9, '+', '(', 5.5, '/', 0.008, ')',
                           '*', '(', 5, '*', '(', 4, '/', 9.7, ')', ')', '-', 9.99]
        self.assertListEqual(scanned_tokens, expected_tokens)

    def test_not_supported_operator(self):
        with self.assertRaises(Exception):
            self.tokenize_input('3 sin 1')


if __name__ == '__main__':
    unittest.main()
