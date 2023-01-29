from src.calculator.Utilities import Utilities

import unittest


class TestScanner(unittest.TestCase):

    def setUp(self):
        self.utility_helper = Utilities()

    def test_is_number(self):
        self.assertTrue(self.utility_helper.is_number('5'))
        self.assertTrue(self.utility_helper.is_number('5.6'))
        self.assertTrue(self.utility_helper.is_number('0.88'))
        self.assertTrue(self.utility_helper.is_number('5345345'))

        self.assertTrue(self.utility_helper.is_number(5345345))
        self.assertTrue(self.utility_helper.is_number(53.54353))

        self.assertFalse(self.utility_helper.is_number('5d345345'))

    def test_is_operator(self):
        self.assertTrue(self.utility_helper.is_operator('+'))
        self.assertTrue(self.utility_helper.is_operator('-'))
        self.assertTrue(self.utility_helper.is_operator('*'))
        self.assertTrue(self.utility_helper.is_operator('/'))

        self.assertFalse(self.utility_helper.is_operator(5))
        self.assertFalse(self.utility_helper.is_operator('44'))
        self.assertFalse(self.utility_helper.is_operator('.'))
        self.assertFalse(self.utility_helper.is_operator('('))
        self.assertFalse(self.utility_helper.is_operator(')'))

    def test_is_parenthesis(self):
        self.assertTrue(self.utility_helper.is_parenthesis(')'))
        self.assertTrue(self.utility_helper.is_parenthesis('('))

        self.assertFalse(self.utility_helper.is_parenthesis('55'))
        self.assertFalse(self.utility_helper.is_parenthesis(55))
        self.assertFalse(self.utility_helper.is_parenthesis('*'))


if __name__ == '__main__':
    unittest.main()
