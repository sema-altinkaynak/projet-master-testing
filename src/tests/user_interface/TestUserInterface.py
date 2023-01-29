from src.exceptions.ParenthesisMissingException import ParenthesisMissingException
from src.exceptions.InputNotValidException import InputNotValidException
from src.user_interface.UserInterface import UserInterface

import unittest


class TestUserInterface(unittest.TestCase):

    def setUp(self):
        self.userinterface = UserInterface(False)
        self.assertEqual(self.userinterface.text.get(), "")

    def test_NumbersEvents(self):
        self.userinterface.text.set("")
        self.userinterface.press9() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "9")
        self.userinterface.press8() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "98")
        self.userinterface.press7() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "987")
        self.userinterface.press6() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "9876")
        self.userinterface.press5() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "98765")
        self.userinterface.press4() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "987654")
        self.userinterface.press3() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "9876543")
        self.userinterface.press2() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "98765432")
        self.userinterface.press1() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "987654321")
        self.userinterface.press0() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "9876543210")
    
    
    def test_MathsEventsAddition(self):
        self.userinterface.text.set("")
        self.userinterface.press1() #Stimulis
        self.userinterface.pressAdd() #Stimulis
        self.userinterface.press1() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "1 + 1")
        
     
    def test_MathsEventsMultiplication(self):
        self.userinterface.text.set("")
        self.userinterface.press1() #Stimulis
        self.userinterface.pressMulti() #Stimulis
        self.userinterface.press1() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "1 * 1")
    
    def test_MathsEventsDivision(self):
        self.userinterface.text.set("")
        self.userinterface.press1() #Stimulis
        self.userinterface.pressDivide() #Stimulis
        self.userinterface.press1() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "1 / 1")
    
    def test_MathsEventSubstraction(self):
        self.userinterface.text.set("")
        self.userinterface.press1() #Stimulis
        self.userinterface.pressMinus() #Stimulis
        self.userinterface.press1() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "1 - 1")
    
    def test_MathsEventNoOperationCase(self):
        self.userinterface.text.set("")
        self.userinterface.pressAccOpen() #Stimulis
        self.userinterface.press1() #Stimulis
        self.userinterface.pressAccClose() #Stimulis
        self.assertEqual(self.userinterface.text.get(), " ( 1 ) ")
    
    def test_MathsEventNoCalculCase(self):
        self.userinterface.text.set("1 + 1")
        self.userinterface.pressClear() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "")

    def test_Calculate(self):
        self.userinterface.text.set("3 * 5 + 16 - 8")
        self.userinterface.pressEqual() #Stimulis
        self.assertEqual(self.userinterface.text.get(), "23.0")
    

if __name__ == '__main__':
    unittest.main()
