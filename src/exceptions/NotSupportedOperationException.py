class NotSupportedOperationException(Exception):
    def __init__(self, *args, op):
        self.operator = op
        super().__init__(args)

    def __str__(self):
        return 'The operation ' + self.operator + ' is not supported.'
