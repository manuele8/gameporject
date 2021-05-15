import unittest
from selenium import webdriver
import page
import values
import time
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
import winsound
d = 0
fh = open("il_mio_file_2.txt", "r")
g = open("il_mio_file_2.txt", "r")
count = 0
array = []
for i in range(len(fh.readlines())):
    array.append(g.readline().split(":")[0])
fh.close()
g.close()
PATH = "C:\Program Files (x86)\chromedriver.exe"
ignored_exceptions=[StaleElementReferenceException, NoSuchElementException]
chromeOptions = Options()
chromeOptions.headless = True

class miamadre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
        self.driver.get("https://www.urban-rivals.com/")

    def test(self):
        global count
        while count < len(array):
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Login()
            PaginaIniziale.Login_Email()
            PaginaIniziale.search_text_element3 = array[count]
            PaginaIniziale.Login_Password()
            PaginaIniziale.search_text_element4 = values.password
            PaginaIniziale.Ad()
            PaginaIniziale.Login_Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
            count += 1
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            break
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

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()



