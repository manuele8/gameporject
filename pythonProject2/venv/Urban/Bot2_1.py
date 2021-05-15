import unittest
from selenium import webdriver
import page
import values
import time
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
import winsound
d = 0
count = 0
array = [9, 8]
vocabolario = {}
PATH = "C:\Program Files (x86)\chromedriver.exe"
ignored_exceptions=[StaleElementReferenceException, NoSuchElementException]
chromeOptions = Options()
chromeOptions.headless = False

class miamadre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
        self.driver.get("https://www.urban-rivals.com/")

    def test(self):
        global count
        counta = 0
        while count < len(array):
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Login()
            PaginaIniziale.Login_Email()
            PaginaIniziale.search_text_element3 = 'giovannimmmmmm70@yopmail.com'
            PaginaIniziale.Login_Password()
            PaginaIniziale.search_text_element4 = values.password
            PaginaIniziale.Ad()
            PaginaIniziale.Login_Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
            Gioca.La_Mia_Collezione()
            elementi = self.driver.find_elements_by_xpath('//div[starts-with(@class, "ur-card card")]')
            for element in elementi:
                li = element.find_element_by_tag_name('img')
                a = element.find_element_by_tag_name('a')
                gigi = li.get_attribute('data-original').split('_')[1].split('_')[0]
                gigo = a.get_attribute('href').split('pj=%23')[1].split('-')[0]
                vocabolario[gigi] = gigo
            print(vocabolario['SAYURA'])
            element = self.driver.find_element_by_xpath('//button[@data-id_perso_joueur=' + vocabolario['SAYURA'] + ']')
            element.click()
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()



