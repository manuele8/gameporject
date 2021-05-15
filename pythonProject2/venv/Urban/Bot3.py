import unittest
from selenium import webdriver
from Urban import page
from Urban import element
import Urban.values
import time
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
array = []
count = 0

def apri_sto_file():
    global array
    fh = open("il_mio_file", "r")
    g = open("il_mio_file", "r")
    for i in range(len(fh.readlines())):
        array.append(g.readline().split(":")[0])
    fh.close()
    g.close()

def printami_sto_profilo():
    global count
    global array
    b = open("profili_fatti", "w")
    b.write(array[count] +"\n")
    b.close()

apri_sto_file()
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
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test2(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            printami_sto_profilo()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test3(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test4(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test5(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test6(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test7(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test8(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test9(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test10(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test11(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test12(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test13(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test14(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()

    def test15(self):
        global count
        while count < len(array):
            print(count)
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
            Gioca.La_Mia_Collezione()
            Collezione = page.Collezione(self.driver)
            Collezione.Ordine_Collezione()
            Collezione.Aggiungi_Clintz_Aggiungi_Esperienza()
            Collezione.Aggiungi_Al_Deck()
            Collezione.Ordine_Decrescente()
            Collezione.Togli_Dal_Deck()
            count += 1
            Collezione.Vendita_Carte()
            Collezione.Ordine_Liv_Max()
            Collezione.Aumenta_E_Vendi_Liv1()
            Collezione.Aumenta_E_Vendi_Liv2()
            Collezione.Aumenta_E_Vendi_Liv3()
            Collezione.Aumenta_E_Vendi_Liv4()
            Collezione.Vendi_Tutto()
            Collezione.Controlla_Cosa_Vendere()
            print("Ho finito per davvero, guarda dove sono")
            Pacchetto = page.Pacchetto(self.driver)
            Pacchetto.Biografia_()
            Biografia = page.Biografia(self.driver)
            Biografia.Disconnessione()
            Biografia.Disconnessione_Conferma()




    def tearDown(self):
        self.driver.close()




if __name__ == '__main__':
    unittest.main()


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


