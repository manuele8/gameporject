import unittest
from selenium import webdriver
import page
import values
import time
from selenium.common.exceptions import *
import winsound
d = 0
PATH = 'C:\Program Files (x86)\geckodriver.exe'
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9150)
ignored_exceptions=[StaleElementReferenceException, NoSuchElementException]
class miamadre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(profile, executable_path=PATH)
        self.driver.get("https://www.urban-rivals.com/")

    def test(self):
        for a in range(0, 5):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Ad()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            if Pacchetto.Moneta():
                Pagina_Email = page.Pagina_Email(self.driver)
                Pagina_Email.Creazione_Mail()
                Pacchetto.Collezione_()
                Pacchetto.La_Mia_Collezione()
                Collezione.Ordine_Collezione()
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
                Mercato = page.Mercato(self.driver)
                Mercato.Vendita_Vansaar()
                Mercato.Vendita_Enigma()
                Mercato.Vendita_Griffonmor()
                Mercato.Vendita_Kate()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)



    def test2(self):
        assert True
        for a in range(5, 10):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test3(self):
        assert True
        for a in range(10, 15):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test4(self):
        assert True
        for a in range(15, 20):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test5(self):
        assert True
        for a in range(25, 30):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test6(self):
        assert True
        for a in range(30, 35):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test7(self):
        assert True
        for a in range(35, 40):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test8(self):
        assert True
        for a in range(40, 45):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)
    def test9(self):
        assert True
        for a in range(45, 50):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)
    def test10(self):
        assert True
        for a in range(50, 55):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test11(self):
        assert True
        for a in range(55, 60):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test12(self):
        assert True
        for a in range(60, 65):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test13(self):
        assert True
        for a in range(65, 70):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)
    def test14(self):
        assert True
        for a in range(70, 75):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test15(self):
        assert True
        for a in range(75, 80):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test16(self):
        assert True
        for a in range(80, 85):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test17(self):
        assert True
        for a in range(85, 90):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test18(self):
        assert True
        for a in range(90, 95):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test19(self):
        assert True
        for a in range(95, 100):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test20(self):
        assert True
        for a in range(100, 105):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test21(self):
        assert True
        for a in range(105, 110):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test22(self):
        assert True
        for a in range(110, 115):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test23(self):
        assert True
        for a in range(115, 120):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test24(self):
        assert True
        for a in range(120, 125):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)

    def test25(self):
        assert True
        for a in range(125, 130):
            global d
            PaginaIniziale = page.PaginaIniziale(self.driver)
            PaginaIniziale.Identificazione()
            PaginaIniziale.Email()
            PaginaIniziale.search_text_element = values.mail_string1 + str(d) + values.mail_string2
            PaginaIniziale.Password()
            PaginaIniziale.search_text_element2 = values.password
            PaginaIniziale.Check_box()
            PaginaIniziale.Gioca_()
            Gioca = page.Gioca(self.driver)
            Gioca.Collezione_()
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
            Negozio.Komboka_Choose()
            Negozio.Acquista_Pacchetto()
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Flip_All()
            Pacchetto.Pack_Value()
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()
            d += 1
        winsound.PlaySound("kik.wav", winsound.SND_ASYNC)
        time.sleep(5)'''

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
