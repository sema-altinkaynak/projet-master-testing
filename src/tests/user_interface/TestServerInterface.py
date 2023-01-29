from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest

# Attention : Indiquez le driver correpondant à votre système d'exploitation
# Attention : Assurez vous d'avoir installé la version 106 de Chrome (l'exécutable avec la bonne version est fourni dans le dossier pour MacOS x86)

class TestServerInterface(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./webdrivers/chromedriverMacOS')
        self.driver.get("http://localhost:8000/1%20+%202")
        self.getElements()

    def tearDown(self):
        self.driver.close()
    
    def getElements(self):
        self.screen = self.driver.find_element(By.ID,"screen")
        self.bt0 = self.driver.find_element(By.ID,"num0")
        self.bt1 = self.driver.find_element(By.ID,"num1")
        self.bt2 = self.driver.find_element(By.ID,"num2")
        self.bt3 = self.driver.find_element(By.ID,"num3")
        self.bt4 = self.driver.find_element(By.ID,"num4")
        self.bt5 = self.driver.find_element(By.ID,"num5")
        self.bt6 = self.driver.find_element(By.ID,"num6")
        self.bt7 = self.driver.find_element(By.ID,"num7")
        self.bt8 = self.driver.find_element(By.ID,"num8")
        self.bt9 = self.driver.find_element(By.ID,"num9")
        self.opAdd = self.driver.find_element(By.ID,"opAdd")
        self.opMin = self.driver.find_element(By.ID,"opMin")
        self.opMult = self.driver.find_element(By.ID,"opMult")
        self.opDiv = self.driver.find_element(By.ID,"opDiv")
        self.parOpen = self.driver.find_element(By.ID,"parOpen")
        self.parClose = self.driver.find_element(By.ID,"parClose")
        self.clear = self.driver.find_element(By.ID,"clear")
        self.equal = self.driver.find_element(By.ID,"equal")

    def test_calcul(self):
        self.assertEqual(self.screen.text, '3.0')
        self.clear.click()
        self.assertEqual(self.screen.text, '0')

    def test_boutons(self):
        self.clear.click()
        self.bt9.click()
        self.assertEqual(self.screen.text, '9')
        self.bt8.click()
        self.assertEqual(self.screen.text, '98')
        self.bt7.click()
        self.assertEqual(self.screen.text, '987')
        self.bt6.click()
        self.assertEqual(self.screen.text, '9876')
        self.bt5.click()
        self.assertEqual(self.screen.text, '98765')
        self.bt4.click()
        self.assertEqual(self.screen.text, '987654')
        self.bt3.click()
        self.assertEqual(self.screen.text, '9876543')
        self.bt2.click()
        self.assertEqual(self.screen.text, '98765432')
        self.bt1.click()
        self.assertEqual(self.screen.text, '987654321')
        self.bt0.click()
        self.assertEqual(self.screen.text, '9876543210')

    def test_opAddition(self):
        self.clear.click()
        self.assertEqual(self.screen.text, '0')
        self.bt1.click()
        self.opAdd.click()
        self.assertEqual(self.screen.text, '1 +')
        self.bt1.click()
        self.assertEqual(self.screen.text, '1 + 1')
        self.bt1.click()
        self.assertEqual(self.screen.text, '1 + 11')

    def test_opSoustraction(self):
        self.clear.click()
        self.assertEqual(self.screen.text, '0')
        self.bt1.click()
        self.opMin.click()
        self.assertEqual(self.screen.text, '1 -')
        self.bt1.click()
        self.assertEqual(self.screen.text, '1 - 1')
        self.bt1.click()
        self.assertEqual(self.screen.text, '1 - 11')

    def test_opDivision(self):
        self.clear.click()
        self.assertEqual(self.screen.text, '0')
        self.bt1.click()
        self.opDiv.click()
        self.assertEqual(self.screen.text, '1 /')
        self.bt1.click()
        self.assertEqual(self.screen.text, '1 / 1')
        self.bt1.click()
        self.assertEqual(self.screen.text, '1 / 11')
    
    def test_opMultiplication(self):
        self.clear.click()
        self.assertEqual(self.screen.text, '0')
        self.bt1.click()
        self.opMult.click()
        self.assertEqual(self.screen.text, '1 *')
        self.bt1.click()
        self.assertEqual(self.screen.text, '1 * 1')
        self.bt1.click()
        self.assertEqual(self.screen.text, '1 * 11')

    def test_opParenthese(self):
        self.clear.click()
        self.assertEqual(self.screen.text, '0')
        self.parOpen.click()
        self.assertEqual(self.screen.text, '(')
        self.bt1.click()
        self.opAdd.click()
        self.assertEqual(self.screen.text, '( 1 +')
        self.bt1.click()
        self.assertEqual(self.screen.text, '( 1 + 1')
        self.parClose.click()
        self.assertEqual(self.screen.text, '( 1 + 1 )')

    def test_history(self):
        lastHistoryEntry = self.driver.find_element(By.ID,"hist0")
        self.assertEqual(lastHistoryEntry.text, '1 + 2 = 3')

if __name__ == '__main__':
    unittest.main()