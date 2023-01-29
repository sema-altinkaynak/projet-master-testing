class Utilities:
   
    def is_number(self, string):
        try:
            float(string)
            return True
        except:
            return False

    def is_operator(self, substring):
        if substring == '+':
            return True
        if substring == '-':
            return True
        if substring == '*':
            return True
        if substring == '/':
            return True
        if substring == '%':
            return True
        return False

    def is_parenthesis(self, string):
        return self.is_opening_parenthesis(string) or self.is_closing_parenthesis(string)

    def is_opening_parenthesis(self, string):
        return string == '('

    def is_closing_parenthesis(self, string):
        return string == ')'
