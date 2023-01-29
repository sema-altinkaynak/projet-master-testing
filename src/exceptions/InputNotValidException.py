class InputNotValidException(Exception):

    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        return 'The input is not valid'
