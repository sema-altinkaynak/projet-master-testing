class ParenthesisMissingException(Exception):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        return 'One parenthesis is missing'
