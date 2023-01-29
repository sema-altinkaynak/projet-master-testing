from src.calculator.FakeScanner import FakeScanner
from src.calculator.FakeParser import FakeParser

import unittest


class TestFakeParser(unittest.TestCase):
    def setUp(self):
        self.parser = FakeParser()
        self.scanner = FakeScanner()

    def tokenize_input(self, input):
        return self.scanner.scan(input)

    def test_parsing_simple_expression_with_negative_number(self):
        tokenized_input = self.tokenize_input('-5 + 5')
        parsedExpression = self.parser.parse(tokenized_input)
        expectedResult = 0
        self.assertEqual(parsedExpression, expectedResult)

    def test_parsing_simple_expression_with_doble_negative_number(self):
        tokenized_input = self.tokenize_input('-5 + -5')
        parsedExpression = self.parser.parse(tokenized_input)
        expectedResult = -10
        self.assertEqual(parsedExpression, expectedResult)

    def test_parsing_simple_expression(self):
        tokenized_input = self.tokenize_input('5 + 5')
        parsedExpression = self.parser.parse(tokenized_input)
        expectedResult = 10
        self.assertEqual(parsedExpression, expectedResult)

    def test_parsing_simple_expression_with_modulo(self):
        tokenized_input = self.tokenize_input('11 % 2')
        parsedExpression = self.parser.parse(tokenized_input)
        expectedResult = 1
        self.assertEqual(parsedExpression, expectedResult)

    def test_parsing_simple_expression_without_multiplication_or_division(self):
        tokenized_input = self.tokenize_input('5 + 5 - 9.1 + 9.9')
        parsedExpression = self.parser.parse(tokenized_input)
        expectedResult = 10.8
        self.assertEqual(parsedExpression, expectedResult)

    def test_parsing_simple_expression_without_multiplication_or_division_and_negative(self):
        tokenized_input = self.tokenize_input('5 + 5 - -9.1 + 9.9')
        parsedExpression = self.parser.parse(tokenized_input)
        expectedResult = 29
        self.assertEqual(parsedExpression, expectedResult)

    def test_parsing_respects_parenthesis(self):
        tokenized_input = self.tokenize_input('5 + ( 2.2 * 3.3 ) + 1')
        parsedExpression = self.parser.parse(tokenized_input)
        expectedResult = 13.26
        self.assertEqual(parsedExpression, expectedResult)

    def test_parsing_respects_nested_parenthesis(self):
        tokenized_input = self.tokenize_input(
            '5 + ( 2 / ( 3 + ( 7 * 1 ) ) ) + 1')
        parsedExpression = self.parser.parse(tokenized_input)
        expectedResult = 6.2
        self.assertEqual(parsedExpression, expectedResult)

    # Testing internal (private) methods

    def test_find_deepest_parenthesis_indices(self):
        tokenized_input = self.tokenize_input(
            '5.1 + ( 2.0 / ( 3 + ( 7.2 * 1 ) ) ) + 1.8')
        opening_parenthesis_index, closing_parenthesis_index = self.parser.find_deepest_parenthesis_indices(
            tokenized_input)
        self.assertEqual(opening_parenthesis_index, 8)
        self.assertEqual(closing_parenthesis_index, 12)

    def test_find_deepest_parenthesis_indices_simple(self):
        tokenized_input = self.tokenize_input(
            '5 + ( 2 / 3 )')
        opening_parenthesis_index, closing_parenthesis_index = self.parser.find_deepest_parenthesis_indices(
            tokenized_input)
        self.assertEqual(opening_parenthesis_index, 2)
        self.assertEqual(closing_parenthesis_index, 6)

    def test_reduce_parenthesis(self):
        tokenized_input = self.tokenize_input(
            '5 + ( 3 / 2 )')
        expected_expression = self.tokenize_input('5 + 1.5')
        reduced_expression = self.parser.reduce_parenthesis(tokenized_input)
        self.assertEqual(reduced_expression, expected_expression)

    def test_parse_expression_without_parenthesis(self):
        tokenized_input = self.tokenize_input('3 + 1 - 1 + 10')
        expression_without_parenthesis = self.parser.parse_expression_without_parenthesis(
            tokenized_input)
        self.assertEqual(expression_without_parenthesis, 13)

    def test_parse_term(self):
        tokenized_input = self.tokenize_input('3 + 1')
        self.assertEqual(self.parser.parse_term(
            tokenized_input[0], tokenized_input[1], tokenized_input[2]), 4)
        tokenized_input = self.tokenize_input('3 - 1')
        self.assertEqual(self.parser.parse_term(
            tokenized_input[0], tokenized_input[1], tokenized_input[2]), 2)
        tokenized_input = self.tokenize_input('3 * 1')
        self.assertEqual(self.parser.parse_term(
            tokenized_input[0], tokenized_input[1], tokenized_input[2]), 3)
        tokenized_input = self.tokenize_input('3 / 1')
        self.assertEqual(self.parser.parse_term(
            tokenized_input[0], tokenized_input[1], tokenized_input[2]), 3)

    def test_does_the_expression_contains_parenthesis(self):
        tokenized_input = self.tokenize_input('3 + 1')
        self.assertFalse(
            self.parser.does_the_expression_contains_parenthesis(tokenized_input))
        tokenized_input = self.tokenize_input('3 + 1 + ( 9 + 1 )')
        self.assertTrue(
            self.parser.does_the_expression_contains_parenthesis(tokenized_input))

    def test_replace_parenthesis_with_the_result(self):
        tokenized_input = self.tokenize_input('5.9 + ( 10 / 2.0 ) + 1')
        expected_result = self.tokenize_input('5.9 + 5 + 1')
        replaced_expression = self.parser.replace_parenthesis_with_the_result(
            2, 6, tokenized_input, 5)
        self.assertEqual(replaced_expression, expected_result)

    def test_not_supported_operator(self):
        with self.assertRaises(Exception):
            tokenized_input = self.tokenize_input('3 sin 1')
            self.parser.parse_term(
                tokenized_input[0], tokenized_input[1], tokenized_input[2])


if __name__ == '__main__':
    unittest.main()
