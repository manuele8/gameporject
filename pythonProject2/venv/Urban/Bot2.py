import unittest
from selenium import webdriver
import page
import element
import values
import time
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
array = []
count = 0

PATH = "C:\Program Files (x86)\chromedriver.exe"
ignored_exceptions=[StaleElementReferenceException, NoSuchElementException]
chromeOptions = Options()
chromeOptions.headless = False


import unittest
class miamadre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
        self.driver.get("https://www.urban-rivals.com/")

    def test(self):
        print(count)
        PaginaIniziale = page.PaginaIniziale(self.driver)
        PaginaIniziale.Identificazione()
        PaginaIniziale.Login()
        PaginaIniziale.Login_Email()
        PaginaIniziale.search_text_element3 = 'manuelson08145@yopmail.com'
        PaginaIniziale.Login_Password()
        PaginaIniziale.search_text_element4 = values.password
        PaginaIniziale.Ad()
        PaginaIniziale.Login_Gioca_()
        Gioca = page.Gioca(self.driver)
        Gioca.Collezione_()
        Gioca.La_Mia_Collezione()
        Gioca.Mastermind()


    def tearDown(self):
        self.driver.close()





'''Mercato = page.Mercato(self.driver)
            Mercato.Vendita_Enigma()
            Mercato.Vendita_Griffonmor()
            Mercato.Vendita_Kate()
            Mercato.Vendita_Memento()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()'''


