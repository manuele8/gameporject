import unittest
from selenium import webdriver
import page
import values
import time
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import winsound
d = 0
PATH = "C:\Program Files (x86)\chromedriver.exe"
ignored_exceptions=[StaleElementReferenceException, NoSuchElementException]
chromeOptions = Options()
chromeOptions.headless = False
prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_experimental_option("prefs", prefs)
class miamadre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
        self.driver.get("https://www.urban-rivals.com/")

    def test(self):
        for a in range(0, 5):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('LMB').key_up(Keys.CONTROL).perform()
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Ad()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
            d += 1
            print(d)
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Vendita_Essie()
            Collezione.Vendita_Essie_Kate()
            Collezione.Vendita_Essie_Confirm()
            Collezione.Vendita_Randy()
            Collezione.Vendita_Randy_Kate()
            Collezione.Vendita_Randy_Confirm()
            Collezione.Negozio_()
            Negozio = page.Negozio(self.driver)
            Negozio.Pacchetto_()
            Negozio.Paradox_Choose()
            Negozio.Skeelz_Choose()
            Negozio.Dominion_Choose()
            Negozio.Berzerk_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            if Pacchetto.Moneta():
                Pagina_Email = page.Pagina_Email(self.driver)
                Pagina_Email.Creazione_Mail()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()