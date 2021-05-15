from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import winsound
from selenium.webdriver.support.ui import WebDriverWait
import Urban.page
import unittest

PATH = "C:\Program Files (x86)\chromedriver.exe"

class miamadre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=PATH)
        self.driver.get("https://www.urban-rivals.com/")

    def test(self):
        PaginaIniziale = Urban.page.PaginaIniziale(self.driver)
        PaginaIniziale.Identificazione()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()