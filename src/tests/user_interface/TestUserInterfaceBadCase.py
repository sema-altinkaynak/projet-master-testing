from src.exceptions.NotSupportedOperationException import NotSupportedOperationException
from src.exceptions.ParenthesisMissingException import ParenthesisMissingException
from src.exceptions.InputNotValidException import InputNotValidException
from src.user_interface.UserInterface import UserInterface

import unittest


class TestUserInterfaceBadCase(unittest.TestCase):

    def setUp(self):
        self.userinterface = UserInterface(False)
        self.assertEqual(self.userinterface.text.get(), "")
    

    def test_OpenParenthesisMissingException(self):
        with self.assertRaises(ParenthesisMissingException):
            self.userinterface.text.set("")
            self.userinterface.press1() #Stimulis
            self.userinterface.pressAccClose() #Stimulis
            self.userinterface.pressEqual() #Stimulis
    
    
    def test_ParenthesisExceptionInComplexCalcul1(self):
        with self.assertRaises(ParenthesisMissingException):
            self.userinterface.text.set("3 * 5 ) + 16 - 8")
            self.userinterface.pressEqual() #Stimulis
    
    
    def test_MissingCloseParenthesisExceptionInComplexCalcul(self):
        with self.assertRaises(ParenthesisMissingException):
            self.userinterface.text.set("( 3 * 5 + 16 - 8")
            self.userinterface.pressEqual() #Stimulis
    
    
    def test_TooMuchParenthesisExceptionInComplexCalcul(self):
        with self.assertRaises(ParenthesisMissingException):
            self.userinterface.text.set("( ( 1 + 1 )")
            self.userinterface.pressEqual() #Stimulis
    

    def test_MathsEventSubstractionParenthesisEsxception(self):
        with self.assertRaises(ParenthesisMissingException):
            self.userinterface.text.set("")
            self.userinterface.press1() #Stimulis
            self.userinterface.pressMinus() #Stimulis
            self.userinterface.press1() #Stimulis
            self.userinterface.pressAccClose() #Stimulis
            self.userinterface.pressEqual() #Stimulis
    
    def test_MathsEvent_Invalid_input_Operator(self):
        with self.assertRaises(ParenthesisMissingException):
            self.userinterface.text.set("")
            self.userinterface.pressAccOpen() #Stimulis
            self.userinterface.press1() #Stimulis
            self.userinterface.pressAccOpen() #Stimulis
            self.userinterface.pressEqual() #Stimulis
    
    def test_MathsEventMultiplicationParenthesisEsxception(self):
        with self.assertRaises(ParenthesisMissingException):
            self.userinterface.text.set("")
            self.userinterface.pressAccOpen() #Stimulis
            self.userinterface.press1() #Stimulis
            self.userinterface.pressAccOpen() #Stimulis
            self.userinterface.pressMulti() #Stimulis
            self.userinterface.press1() #Stimulis
            self.userinterface.pressAccClose() #Stimulis
            self.userinterface.pressEqual() #Stimulis
    
    def test_MathsEvent_Invalid_input_only_one_number(self):
        with self.assertRaises(InputNotValidException):
            self.userinterface.text.set("")
            self.userinterface.press1() #Stimulis
            self.userinterface.pressEqual() #Stimulis

    def test_MathsEventMultiplicationInvalidExpression(self):
        with self.assertRaises(InputNotValidException):
            self.userinterface.text.set("")
            self.userinterface.press1() #Stimulis
            self.userinterface.pressAccOpen() #Stimulis
            self.userinterface.pressMulti() #Stimulis
            self.userinterface.press1() #Stimulis
            self.userinterface.pressAccClose() #Stimulis
            self.userinterface.pressEqual() #Stimulis
    
    def test_MathsEvent_InputWithoutOperationWithParenthesis(self):
        with self.assertRaises(InputNotValidException):
            self.userinterface.text.set("")
            self.userinterface.pressAccOpen() #Stimulis
            self.userinterface.press1() #Stimulis
            self.userinterface.press6() #Stimulis
            self.userinterface.pressAccClose() #Stimulis
            self.userinterface.pressEqual() #Stimulis
    
    def test_MathsEvent_SimpleInputWithoutOperationwithoutParenthesis(self):
        with self.assertRaises(InputNotValidException):
            self.userinterface.text.set("")
            self.userinterface.press1() #Stimulis
            self.userinterface.press6() #Stimulis
            self.userinterface.pressEqual() #Stimulis
    
    def test_missingSpaces(self):
        with self.assertRaises(InputNotValidException):
            self.userinterface.text.set("35 + 4 (4 / 7 )")
            self.userinterface.pressEqual() #Stimulis
    
    def test_InputWithoutOperationAfterParenthesis(self):
        with self.assertRaises(InputNotValidException):
            self.userinterface.text.set("35 + 4 ( 4 / 7 )")
            self.userinterface.pressEqual() #Stimulis

    def test_notSupportedOperation(self):
        with self.assertRaises(Exception):
            self.userinterface.text.set("3 sin 1")
            self.userinterface.pressEqual() #Stimulis
    
    
    

if __name__ == '__main__':
    unittest.main()