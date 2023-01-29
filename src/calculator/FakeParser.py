from src.exceptions.NotSupportedOperationException import NotSupportedOperationException
from src.calculator.Utilities import Utilities


class FakeParser:

    def __init__(self) -> None:
        self.utility_helper = Utilities()

    def parse(self, tokens):
        reduced_expression = self.reduce_parenthesis(tokens)
        return self.parse_expression_without_parenthesis(reduced_expression)

    def reduce_parenthesis(self, tokens):
        expression = [t for t in tokens]

        while self.does_the_expression_contains_parenthesis(expression):
            deepest_opening_parenthesis, deepest_closing_parenthesis = self.find_deepest_parenthesis_indices(
                expression)
            parsed_internal_expression = self.parse_expression_without_parenthesis(
                expression[deepest_opening_parenthesis + 1: deepest_closing_parenthesis])
            expression = self.replace_parenthesis_with_the_result(
                deepest_opening_parenthesis, deepest_closing_parenthesis, expression, parsed_internal_expression)
        return expression

    def replace_parenthesis_with_the_result(self, opening_parenthesis_index, closing_parenthesis_index, expression, parsed_expression):
        expression_before_parenthesis = [expression[i]
                                         for i in range(opening_parenthesis_index)]
        replaced_expression = expression_before_parenthesis
        replaced_expression.append(parsed_expression)
        expression_after_parenthesis = [expression[i] for i in range(
            closing_parenthesis_index + 1, len(expression))]
        return replaced_expression + expression_after_parenthesis

    # In the current version of this parser, we must have a number after an operator.
    # An there cannot be two consecutive numbers.
    # So, an expression will look like this: n1 operator1 n2 operator2 n3 ...
    # An expression will have at least 2 numbers and one operator.
    # The impar indexes will be numbers and the pair will be operators.
    ##
    # Note that this algorithm needs to be updated if we add support for operators that take only one parameter
    # For example sin, cos, tan ...

    def parse_expression_without_parenthesis(self, tokens):
        result_of_evaluation = self.parse_term(tokens[0], tokens[1], tokens[2])
        counter = 3
        while (counter < len(tokens)):
            result_of_evaluation = self.parse_term(
                result_of_evaluation, tokens[counter], tokens[counter + 1])
            counter = counter + 2
        return result_of_evaluation

    # A minimal term must have at least 2 numbers and 1 operator
    #
    # Instead of having this ifs, we can have polymorphic objects and just dispatch the message.
    # For example: operator.execute(left_side, right_side)
    #
    # Note that this will change if we add support for operators that take only one parameter.
    # Like sqrt ...
    def parse_term(self, left_side, operator, right_side):
        if operator == '+':
            return left_side + right_side
        if operator == '-':
            return left_side - right_side
        if operator == '*':
            return left_side * right_side
        if operator == '/':
            return left_side / right_side
        if operator == '%':
            return left_side % right_side
        raise NotSupportedOperationException(operator)

    def does_the_expression_contains_parenthesis(self, tokens):
        response = False
        for token in tokens:
            if self.utility_helper.is_parenthesis(token):
                response = True
        return response

    def find_deepest_parenthesis_indices(self, tokens):
        # Get the last occurence of the opening parenthesis. First, get an array with only the indices of the ocurrences.
        #Then, take the last element as it is the last occurrence
        opening_parenthesis_index = [idx for idx, each in enumerate(
            tokens) if each == '('][-1]
        closing_parenthesis_index = tokens.index(
            ')', opening_parenthesis_index)
        return opening_parenthesis_index, closing_parenthesis_index
