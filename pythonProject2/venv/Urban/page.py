from element import BasePageElement
from element import BasePageElement2
from element import BasePageElement3
from element import BasePageElement4
from locator import PaginaInizialeLocators
from locator import GiocaLocators
from locator import CollezioneLocators
from locator import NegozioLocators
from locator import PacchettoLocators
from locator import BiografiaLocators
from locator import EmailLocators
from locator import MercatoLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import values
import time
import winsound

count = 0
Clintz = 15000
Punti_Esperienza = 0
Money = False
kosnikai = False
Puoi_Vendere = False
Vansaar = False
Enigma = False
Griffonmor = False
Kate = False
Memento = False
Nadia = False
Miss_Denna = False

def Esperienza():
    vocabolario = {13: 2, 32: 3, 69: 4, 130: 5, 221: 6, 348: 7, 517: 8, 734: 9, 1005: 10}
    for i in range(len(vocabolario)-1):
        if Punti_Esperienza > list(vocabolario)[i] and Punti_Esperienza < list(vocabolario)[i+1]:
            return vocabolario[list(vocabolario)[i]]
        elif Punti_Esperienza > 1005:
            return 10

class SearchTextElement(BasePageElement):
    locator = '//*[@id="register"]/form/div[1]/input'

class SearchTextElement2(BasePageElement2):
    locator2 = '//*[@id="register"]/form/div[2]/input'

class SearchTextElement3(BasePageElement3):
    locator3 = '//*[@id="login"]/form/div[1]/input'

class SearchTextElement4(BasePageElement4):
    locator4 = '//*[@id="login"]/form/div[2]/input'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver



class PaginaIniziale(BasePage):
    search_text_element = SearchTextElement()
    search_text_element2 = SearchTextElement2()
    search_text_element3 = SearchTextElement3()
    search_text_element4 = SearchTextElement4()

    def Identificazione(self):
        global Clintz
        global Punti_Esperienza
        Punti_Esperienza = 0
        Clintz = 15000
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PaginaInizialeLocators.IDENTIFICATI_BOTTONE))
        element = self.driver.find_element(*PaginaInizialeLocators.IDENTIFICATI_BOTTONE)
        element.click()

    def Login(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PaginaInizialeLocators.IDENTIFICATI))
        element = self.driver.find_element(*PaginaInizialeLocators.IDENTIFICATI)
        element.click()

    def Email(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PaginaInizialeLocators.EMAIL_CAMPO))
        element = self.driver.find_element(*PaginaInizialeLocators.EMAIL_CAMPO)
        element.click()

    def Login_Email(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PaginaInizialeLocators.LOGIN_EMAIL_CAMPO))
        element = self.driver.find_element(*PaginaInizialeLocators.LOGIN_EMAIL_CAMPO)
        element.click()

    def Password(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PaginaInizialeLocators.PASSWORD_CAMPO))
        element = self.driver.find_element(*PaginaInizialeLocators.PASSWORD_CAMPO)
        element.click()

    def Login_Password(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PaginaInizialeLocators.LOGIN_PASSWORD_CAMPO))
        element = self.driver.find_element(*PaginaInizialeLocators.LOGIN_PASSWORD_CAMPO)
        element.click()

    def Check_box(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PaginaInizialeLocators.CHECK_BOX))
        element = self.driver.find_element(*PaginaInizialeLocators.CHECK_BOX)
        element.click()

    def Ad(self):
        try:
            element = self.driver.find_element(*PaginaInizialeLocators.AD_OK_BOTTONE)
            element.click()
        except:
            pass

    def Gioca_(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PaginaInizialeLocators.GIOCA_BOTTONE))
        element = self.driver.find_element(*PaginaInizialeLocators.GIOCA_BOTTONE)
        element.click()

    def Login_Gioca_(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PaginaInizialeLocators.LOGIN_GIOCA_BOTTONE))
        element = self.driver.find_element(*PaginaInizialeLocators.LOGIN_GIOCA_BOTTONE)
        element.click()

    def Gioca_Check(self):
        return WebDriverWait(self.driver, 20).until(
            lambda driver: driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE))

class Gioca(BasePage):
    search_text_element = SearchTextElement()

    def Collezione_(self):
        global count
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE))
        element = self.driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE)
        element.click()
        count += 1
        print(count)

    def La_Mia_Collezione(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE))
        element = self.driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE)
        element.click()

    def Vendita_Essie_Check(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.VENDITA_ESSIE_BOTTONE))

    def Mastermind(self):
        self.driver.get('https://www.urban-rivals.com/it/community/forum/?mode=viewsubject&id_subject=2768884')
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*GiocaLocators.MASTERMIND_TESTO))
        element = self.driver.find_element(*GiocaLocators.MASTERMIND_TESTO).text
        print(element)
        a = 0
        array9 = []
        while 1:
            for i in range(1, 100):
                try:
                    element = self.driver.find_element_by_xpath('/html/body/div[3]/ul[4]/li[' + str(i) + ']')
                except:
                    a = (i - 1)
                    array9.append(a)
                    if len(array9) > 2:
                        array9.pop(0)
                    break
            c = len(array9)
            if c > 1:
                if array9[c - 2] != array9[c - 1]:
                    winsound.PlaySound('Cow.wav', winsound.SND_FILENAME)
                else:
                    time.sleep(2)
                    self.driver.get('https://www.urban-rivals.com/it/community/forum/?mode=viewsubject&id_subject=2768884')
            print(array9)
class Collezione(BasePage):
    search_text_element = SearchTextElement()

    def Vendita_Essie(self):
        global Punti_Esperienza
        global Clintz
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.VENDITA_ESSIE_BOTTONE))
        element = self.driver.find_element(*CollezioneLocators.VENDITA_ESSIE_BOTTONE)
        element.click()

    def Vendita_Essie_Kate(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.VENDITA_ESSIE_TOKATE))
        element = self.driver.find_element(*CollezioneLocators.VENDITA_ESSIE_TOKATE)
        element.click()

    def Vendita_Essie_Confirm(self):
        global Clintz
        global Punti_Esperienza
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA))
        element = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
        element.click()
        Clintz += 2500
        Punti_Esperienza += 50
        print(Clintz)
        print(Punti_Esperienza)

    def Vendita_Randy(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.CONTROLLO_).text == values.name1)
        except:
            print("Fiuu1")
            time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.VENDITA_RANDY_BOTTONE))
        element = self.driver.find_element(*CollezioneLocators.VENDITA_RANDY_BOTTONE)
        element.click()

    def Vendita_Randy_Kate(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.VENDITA_RANDY_TOKATE))
        element = self.driver.find_element(*CollezioneLocators.VENDITA_RANDY_TOKATE)
        element.click()

    def Vendita_Randy_Confirm(self):
        global Clintz
        global Punti_Esperienza
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA))
        element = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
        element.click()
        Clintz += 2500
        Punti_Esperienza += 50
        print(Clintz)
        print(Punti_Esperienza)

    def Aggiungi_Clintz_Aggiungi_Esperienza(self):
        global Clintz
        global Punti_Esperienza
        Clintz += 5000
        Punti_Esperienza += 100

    def Negozio_(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.CONTROLLO_).text == values.name2)
        except:
            print("Fiuu2")
            time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.NEGOZIO_BOTTONE))
        element = self.driver.find_element(*CollezioneLocators.NEGOZIO_BOTTONE)
        element.click()

    def Pacchetto_Check(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*NegozioLocators.PACCHETTO_BOTTONE))

    def Ordine_Collezione(self):
        print("ordine")
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.ORDINE_RARITA_BOTTONE))
        element = self.driver.find_element(*CollezioneLocators.ORDINE_RARITA_BOTTONE)
        element.click()
        element = self.driver.find_element(*CollezioneLocators.FUORI_DAL_DECK_BOTTONE)
        element.click()
        element = self.driver.find_element(*CollezioneLocators.NUMERO_CARTE_BOTTONE_BLUFF)
        element.click()
        element = self.driver.find_element(*CollezioneLocators.NUMERO_CARTE_BOTTONE)
        element.click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.find_elements(*CollezioneLocators.CHECK_NUMERO_CARTE)) > 12)

    def Aggiungi_Al_Deck(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.AGGIUNGI_AL_DECK_BOTTONE2))
        elements = self.driver.find_elements(*CollezioneLocators.AGGIUNGI_AL_DECK_BOTTONE)
        print(len(elements))
        print(elements)
        try:
            for i in range(len(elements)):
                self.driver.execute_script("arguments[0].click();", elements[i])
        except StaleElementReferenceException as Exception:
            print("Vediamo se supero le eccezioni")
            elements = self.driver.find_elements(*CollezioneLocators.AGGIUNGI_AL_DECK_BOTTONE)
            for i in range(len(elements)):
                self.driver.execute_script("arguments[0].click();", elements[i])

        print("ci sono")
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(*CollezioneLocators.AGGIUNGI_AL_DECK_BOTTONE) == [])

    def Ordine_Decrescente(self):
        print("ordine decrescente")
        nome1 = self.driver.find_element(*CollezioneLocators.NOMI_CARTE).text
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.ORDINE_DECRESCENTE_BOTTONE))
        element = self.driver.find_element(*CollezioneLocators.ORDINE_DECRESCENTE_BOTTONE)
        element.click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.NOME_PRIMA_CARTA).text != nome1)


    def Togli_Dal_Deck(self):
        print("togli")
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.TOGLI_DAL_DECK_BOTTONE))
        elements = self.driver.find_elements(*CollezioneLocators.TOGLI_DAL_DECK_BOTTONE)
        for i in range(1, len(elements) - 7):
            elements[i - 1].click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.find_elements(*CollezioneLocators.TOGLI_DAL_DECK_BOTTONE)) == 8)

    def Vendita_Carte(self):
        global Punti_Esperienza
        global Clintz
        print("vendita")
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.PRIMO_BOTTONE_VENDITA))
        array2 = []
        elements = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
        for g in range(len(elements)):
            f = self.driver.find_elements(*CollezioneLocators.NOMI_CARTE)
            array2.append(f[g].text)
        print(array2)
        print("sono qui")
        for m in range(25):
            elements = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
            print("asmd")
            if len(elements) == 8:
                break
            element = self.driver.find_element(*CollezioneLocators.PRIMO_BOTTONE_VENDITA)
            print("qui")
            self.driver.execute_script("arguments[0].click();", element)
            print("clicco")
            try:
                comune = self.driver.find_element(*CollezioneLocators.COMUNE_BOTTONE)
                print("comune")
            except:
                comune = False
            try:
                non_comune = self.driver.find_element(*CollezioneLocators.NON_COMUNE_BOTTONE)
                print("non comune")
            except:
                non_comune = False
            try:
                rara = self.driver.find_element(*CollezioneLocators.RARA_BOTTONE)
                print("rara")
            except:
                rara = False
            if comune or non_comune or rara:
                if comune:
                    comune.click()
                    print("sono qui")
                    Clintz += 250
                    Punti_Esperienza += 10
                    print(Clintz)
                    print(Punti_Esperienza)
                elif non_comune:
                    print("sono qui ma non comune")
                    non_comune.click()
                    Clintz += 2500
                    Punti_Esperienza += 50
                    print(Clintz)
                    print(Punti_Esperienza)
                else:
                    print("rara ma qui")
                    rara.click()
                    Clintz += 9000
                    Punti_Esperienza += 100
                    print(Clintz)
                    print(Punti_Esperienza)
                print("ok")
                elemento = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
                print("ok3")
                elemento.click()
                print("ok4")
                print(self.driver.find_element(*CollezioneLocators.NOMI_CARTE).text == array2[m + 1])
                for i in range(5):
                    try:
                        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*CollezioneLocators.NOMI_CARTE))
                        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*CollezioneLocators.NOMI_CARTE).text == array2[m+1])
                        break
                    except:
                        print("Fiuu qui")
                        time.sleep(1)

    def Ordine_Liv_Max(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.ORDINE_LIVELLO_MASSIMO_BOTTONE))
        element = self.driver.find_element(*CollezioneLocators.ORDINE_LIVELLO_MASSIMO_BOTTONE)
        element.click()
        element = self.driver.find_element(*CollezioneLocators.ORDINE_CRESCENTE_BOTTONE)
        element.click()
        element = self.driver.find_element(*CollezioneLocators.ORDINE_FUORI_DAL_DECK_BOTTONE)
        element.click()
        for i in range(3):
            try:
                WebDriverWait(self.driver, 5).until(
                    lambda driver: driver.find_elements(*CollezioneLocators.TOGLI_DAL_DECK_BOTTONE) == [])
                break
            except:
                element = self.driver.find_element(*CollezioneLocators.ORDINE_SOLO_EVOLUZIONE_COMP_BOTTONE)
                element.click()
                element = self.driver.find_element(*CollezioneLocators.ORDINE_FUORI_DAL_DECK_BOTTONE)
                element.click()

    def Aumenta_E_Vendi_Liv1(self):
        global Punti_Esperienza
        global Clintz
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE) != [])
        elements = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
        elements[len(elements) - 1].click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA))
        cancella_elemento = self.driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA)
        cancella_elemento.click()
        asinf = True
        while asinf:
            print("Primo loop")
            arraynames_liv1 = []
            arraylinks_liv1 = []
            arraylevels_liv1 = []
            upgrades_liv1 = self.driver.find_elements(*CollezioneLocators.UPGRADE_BOTTONE)
            sells_liv1  = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
            names_liv1 = self.driver.find_elements(*CollezioneLocators.NOMI_CARTE)
            for i in range(0, len(sells_liv1)):
                arraynames_liv1.append(names_liv1[i].text)
            images_liv1 = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
            for r in range(len(images_liv1)):
                link = images_liv1[r].get_attribute('src')
                arraylinks_liv1.append(link)
            try:
                for testo in arraylinks_liv1:
                    livello = testo.split("_")[2].split("N")[1]
                    arraylevels_liv1.append(int(livello))
            except:
                arraylinks_liv1 = []
                arraylevels_liv1 = []
                elements = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
                elements[len(elements) - 1].click()
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA))
                cancella_elemento = self.driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA)
                cancella_elemento.click()
                images_liv1 = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
                for r in range(len(images_liv1)):
                    link = images_liv1[r].get_attribute('src')
                    arraylinks_liv1.append(link)
                for testo in arraylinks_liv1:
                    livello = testo.split("_")[2].split("N")[1]
                    arraylevels_liv1.append(int(livello))
            print(arraylevels_liv1)
            contatore_liv1 = 0
            index_liv1 = 0
            for i in range(len(arraylevels_liv1)):
                if arraylevels_liv1[i] == 1:
                    contatore_liv1 += 1
                    index_liv1 = i
                    break
            if contatore_liv1 == 0:
                break
            nome_carta_upgrade = arraynames_liv1[index_liv1]
            upgrades_liv1[index_liv1].click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.UPGRADE_CONFERMA_BOTTONE))
            upgrade_conferma_liv1 = self.driver.find_element(*CollezioneLocators.UPGRADE_CONFERMA_BOTTONE)
            self.driver.execute_script("arguments[0].click();", upgrade_conferma_liv1)
            rimpiazzo_liv1 = arraylinks_liv1[index_liv1].replace('_N1_', '_N2_')
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzo_liv1 + '\"]'))
            Punti_Esperienza += 20
            Clintz -= 1000
            arraynames_liv1 = []
            arraylinks_liv1 = []
            upgrades2_liv1 = self.driver.find_elements(*CollezioneLocators.UPGRADE_BOTTONE)
            sells2_liv1 = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
            names2_liv1 = self.driver.find_elements(*CollezioneLocators.NOMI_CARTE)
            for i in range(0, len(sells2_liv1)):
                arraynames_liv1.append(names2_liv1[i].text)
            images_liv1 = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
            for r in range(len(images_liv1)):
                link = images_liv1[r].get_attribute('src')
                arraylinks_liv1.append(link)
            index2_liv1 = arraylinks_liv1.index(rimpiazzo_liv1)
            if len(upgrades2_liv1) < len(upgrades_liv1) or ((len(upgrades2_liv1) - len(upgrades_liv1)) != (len(sells2_liv1) - len(sells_liv1))):
                sells2_liv1[index2_liv1].click()
                try:
                    comune = self.driver.find_element(*CollezioneLocators.COMUNE_BOTTONE)
                    print("comune")
                except:
                    comune = False
                try:
                    non_comune = self.driver.find_element(*CollezioneLocators.NON_COMUNE_BOTTONE)
                    print("non comune")
                except:
                    non_comune = False
                try:
                    rara = self.driver.find_element(*CollezioneLocators.RARA_BOTTONE)
                    print("rara")
                except:
                    rara = False
                if comune or non_comune or rara:
                    if comune:
                        comune.click()
                        print("sono qui")
                        Clintz += 250
                        Punti_Esperienza += 10
                    elif non_comune:
                        print("sono qui ma non comune")
                        non_comune.click()
                        Clintz += 2500
                        Punti_Esperienza += 50
                    else:
                        print("rara ma qui")
                        rara.click()
                        Clintz += 9000
                        Punti_Esperienza += 1000
                    print("ok")
                    elemento_conferma = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
                    print("ok3")
                    elemento_conferma.click()
                    WebDriverWait(self.driver, 10).until(
                        lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzo_liv1 + '\"]') == [])
        print(Punti_Esperienza)
        print(Clintz)

    def Aumenta_E_Vendi_Liv2(self):
        global Punti_Esperienza
        global Clintz
        liv1 = False
        asinfo = True
        while asinfo:
            print("Secondo loop")
            arraynames_liv2 = []
            arraylinks_liv2 = []
            arraylevels_liv2 = []
            upgrades_liv2 = self.driver.find_elements(*CollezioneLocators.UPGRADE_BOTTONE)
            sells_liv2  = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
            names_liv2 = self.driver.find_elements(*CollezioneLocators.NOMI_CARTE)
            for i in range(0, len(sells_liv2)):
                arraynames_liv2.append(names_liv2[i].text)
            images_liv2 = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
            for r in range(len(images_liv2)):
                link = images_liv2[r].get_attribute('src')
                arraylinks_liv2.append(link)
            try:
                for testo in arraylinks_liv2:
                    livello = testo.split("_")[2].split("N")[1]
                    arraylevels_liv2.append(int(livello))
            except:
                arraylinks_liv2 = []
                arraylevels_liv2 = []
                elements = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
                elements[len(elements) - 1].click()
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA))
                cancella_elemento = self.driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA)
                cancella_elemento.click()
                images_liv2 = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
                for r in range(len(images_liv2)):
                    link = images_liv2[r].get_attribute('src')
                    arraylinks_liv2.append(link)
                for testo in arraylinks_liv2:
                    livello = testo.split("_")[2].split("N")[1]
                    arraylevels_liv2.append(int(livello))
            print(arraylevels_liv2)
            contatore_liv2 = 0
            index_liv2 = 0
            for i in range(len(arraylevels_liv2)):
                if arraylevels_liv2[i] == 2:
                    contatore_liv2 += 1
                    index_liv2 = i
                    break
                elif arraylevels_liv2[i] == 1:
                    contatore_liv2 += 1
                    index_liv2 = i
                    liv1 = True
                    break
            if contatore_liv2 == 0:
                break
            nome_carta_upgrade = arraynames_liv2[index_liv2]
            upgrades_liv2[index_liv2].click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.UPGRADE_CONFERMA_BOTTONE))
            upgrade_conferma_liv2 = self.driver.find_element(*CollezioneLocators.UPGRADE_CONFERMA_BOTTONE)
            self.driver.execute_script("arguments[0].click();", upgrade_conferma_liv2)
            rimpiazzo_liv1 = arraylinks_liv2[index_liv2].replace('_N1_', '_N2_')
            rimpiazzo_liv2 = arraylinks_liv2[index_liv2].replace('_N2_', '_N3_')
            if liv1:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzo_liv1 + '\"]'))
                Punti_Esperienza += 20
                Clintz -= 1000
            else:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzo_liv2 + '\"]'))
                Punti_Esperienza += 30
                Clintz -= 3000
            arraynames_liv2 = []
            arraylinks_liv2 = []
            upgrades2_liv2 = self.driver.find_elements(*CollezioneLocators.UPGRADE_BOTTONE)
            sells2_liv2 = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
            names2_liv2 = self.driver.find_elements(*CollezioneLocators.NOMI_CARTE)
            for i in range(0, len(sells2_liv2)):
                arraynames_liv2.append(names2_liv2[i].text)
            images_liv2 = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
            for r in range(len(images_liv2)):
                link = images_liv2[r].get_attribute('src')
                arraylinks_liv2.append(link)
            if liv1:
                index2_liv2 = arraylinks_liv2.index(rimpiazzo_liv1)
            else:
                index2_liv2 = arraylinks_liv2.index(rimpiazzo_liv2)
            if len(upgrades2_liv2) < len(upgrades_liv2) or ((len(upgrades2_liv2) - len(upgrades_liv2)) != (len(sells2_liv2) - len(sells_liv2))):
                sells2_liv2[index2_liv2].click()
                try:
                    comune = self.driver.find_element(*CollezioneLocators.COMUNE_BOTTONE)
                    print("comune")
                except:
                    comune = False
                try:
                    non_comune = self.driver.find_element(*CollezioneLocators.NON_COMUNE_BOTTONE)
                    print("non comune")
                except:
                    non_comune = False
                try:
                    rara = self.driver.find_element(*CollezioneLocators.RARA_BOTTONE)
                    print("rara")
                except:
                    rara = False
                if comune or non_comune or rara:
                    if comune:
                        comune.click()
                        print("sono qui")
                        Clintz += 250
                        Punti_Esperienza += 10
                    elif non_comune:
                        print("sono qui ma non comune")
                        non_comune.click()
                        Clintz += 2500
                        Punti_Esperienza += 50
                    else:
                        print("rara ma qui")
                        rara.click()
                        Clintz += 9000
                        Punti_Esperienza += 100
                    print("ok")
                    elemento_conferma = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
                    print("ok3")
                    elemento_conferma.click()
                    if liv1:
                        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzo_liv1 + '\"]') == [])
                    else:
                        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzo_liv2 + '\"]') == [])
        print(Punti_Esperienza)
        print(Clintz)

    def Aumenta_E_Vendi_Liv3(self):
        global Punti_Esperienza
        global Clintz
        global kosnikai
        global Puoi_Vendere
        livello_ = Esperienza()
        Clintz += 2000 * (livello_ - 1)
        liv1 = False
        liv2 = False
        asinfof = True
        while asinfof:
            print("Terzo loop")
            livello_inizio = Esperienza()
            arraynames_liv3 = []
            arraylinks_liv3 = []
            arraylevels_liv3 = []
            upgrades_liv3 = self.driver.find_elements(*CollezioneLocators.UPGRADE_BOTTONE)
            sells_liv3  = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
            names_liv3 = self.driver.find_elements(*CollezioneLocators.NOMI_CARTE)
            for i in range(0, len(sells_liv3)):
                arraynames_liv3.append(names_liv3[i].text)
            images_liv3 = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
            for r in range(len(images_liv3)):
                link = images_liv3[r].get_attribute('src')
                arraylinks_liv3.append(link)
            try:
                for testo in arraylinks_liv3:
                    livello = testo.split("_")[2].split("N")[1]
                    arraylevels_liv3.append(int(livello))
            except:
                arraylinks_liv3 = []
                arraylevels_liv3 = []
                elements = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
                elements[len(elements) - 1].click()
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA))
                cancella_elemento = self.driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA)
                cancella_elemento.click()
                images_liv3 = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
                for r in range(len(images_liv3)):
                    link = images_liv3[r].get_attribute('src')
                    arraylinks_liv3.append(link)
                for testo in arraylinks_liv3:
                    livello = testo.split("_")[2].split("N")[1]
                    arraylevels_liv3.append(int(livello))
            print(arraylevels_liv3)
            contatore_liv3 = 0
            index_liv3 = 0
            for i in range(len(arraylevels_liv3)):
                if arraylevels_liv3[i] == 3:
                    contatore_liv3 += 1
                    index_liv3 = i
                    break
                elif arraylevels_liv3[i] == 2:
                    contatore_liv3 += 1
                    index_liv3 = i
                    liv2 = True
                    break
                elif arraylevels_liv3[i] == 1:
                    contatore_liv3 += 1
                    index_liv3 = i
                    liv1 = True
                    break
            if contatore_liv3 == 0:
                break
            if liv1 and Clintz < 1000:
                print("Non mi bastano i clintz")
                break
            if liv2 and Clintz < 3000:
                print("Non mi bastano i clintz")
                break
            if not (liv1 or liv2) and Clintz < 6000:
                print("Non mi bastano i clintz")
                break
            nome_carta_upgrade = arraynames_liv3[index_liv3]
            upgrades_liv3[index_liv3].click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.UPGRADE_CONFERMA_BOTTONE))
            upgrade_conferma_liv3 = self.driver.find_element(*CollezioneLocators.UPGRADE_CONFERMA_BOTTONE)
            self.driver.execute_script("arguments[0].click();", upgrade_conferma_liv3)
            rimpiazzo_liv1 = arraylinks_liv3[index_liv3].replace('_N1_', '_N2_')
            rimpiazzo_liv2 = arraylinks_liv3[index_liv3].replace('_N2_', '_N3_')
            rimpiazzo_liv3 = arraylinks_liv3[index_liv3].replace('_N3_', '_N4_')
            if liv1:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzo_liv1 + '\"]'))
                Punti_Esperienza += 20
                Clintz -= 1000
            if liv2:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzo_liv2 + '\"]'))
                Punti_Esperienza += 30
                Clintz -= 3000
            else:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzo_liv3 + '\"]'))
                Punti_Esperienza += 40
                Clintz -= 6000
            livello_evoluzione = Esperienza()
            Clintz += 2000 * (livello_evoluzione - livello_inizio)
            if Punti_Esperienza >= 1005:
                kosnikai = True
                Puoi_Vendere = True
                print("Io mi fermo qui!")
                break
            arraynames_liv3 = []
            arraylinks_liv3 = []
            upgrades2_liv3 = self.driver.find_elements(*CollezioneLocators.UPGRADE_BOTTONE)
            sells2_liv3 = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
            names2_liv3 = self.driver.find_elements(*CollezioneLocators.NOMI_CARTE)
            for i in range(0, len(sells2_liv3)):
                arraynames_liv3.append(names2_liv3[i].text)
            images_liv3 = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
            for r in range(len(images_liv3)):
                link = images_liv3[r].get_attribute('src')
                arraylinks_liv3.append(link)
            if liv1:
                index2_liv3 = arraylinks_liv3.index(rimpiazzo_liv1)
            if liv2:
                index2_liv3 = arraylinks_liv3.index(rimpiazzo_liv2)
            else:
                index2_liv3 = arraylinks_liv3.index(rimpiazzo_liv3)
            if len(upgrades2_liv3) < len(upgrades_liv3) or ((len(upgrades2_liv3) - len(upgrades_liv3)) != (len(sells2_liv3) - len(sells_liv3))):
                sells2_liv3[index2_liv3].click()
                try:
                    comune = self.driver.find_element(*CollezioneLocators.COMUNE_BOTTONE)
                    print("comune")
                except:
                    comune = False
                try:
                    non_comune = self.driver.find_element(*CollezioneLocators.NON_COMUNE_BOTTONE)
                    print("non comune")
                except:
                    non_comune = False
                try:
                    rara = self.driver.find_element(*CollezioneLocators.RARA_BOTTONE)
                    print("rara")
                except:
                    rara = False
                if comune or non_comune or rara:
                    if comune:
                        comune.click()
                        print("sono qui")
                        Clintz += 250
                        Punti_Esperienza += 10
                    elif non_comune:
                        print("sono qui ma non comune")
                        non_comune.click()
                        Clintz += 2500
                        Punti_Esperienza += 50
                    else:
                        print("rara ma qui")
                        rara.click()
                        Clintz += 9000
                        Punti_Esperienza += 100
                    livello_vendita = Esperienza()
                    Clintz += 2000 * (livello_vendita - livello_evoluzione)
                    print("ok")
                    elemento_conferma = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
                    print("ok3")
                    elemento_conferma.click()
                    if liv1:
                        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzo_liv1 + '\"]') == [])
                    if liv2:
                        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzo_liv2 + '\"]') == [])
                    else:
                        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzo_liv3 + '\"]') == [])
            if Punti_Esperienza >= 1005:
                kosnikai = True
                Puoi_Vendere = True
                print("Io mi fermo qui!")
                break
        print(Punti_Esperienza)
        print(Clintz)

    def Aumenta_E_Vendi_Liv4(self):
        global Punti_Esperienza
        global Clintz
        global kosnikai
        global Puoi_Vendere
        liv1 = False
        liv2 = False
        liv3 = False
        asinfofo = True
        while asinfofo and not kosnikai:
            print("Quarto loop")
            livello_inizio = Esperienza()
            arraynames_liv4 = []
            arraylinks_liv4 = []
            arraylevels_liv4 = []
            upgrades_liv4 = self.driver.find_elements(*CollezioneLocators.UPGRADE_BOTTONE)
            sells_liv4  = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
            names_liv4 = self.driver.find_elements(*CollezioneLocators.NOMI_CARTE)
            for i in range(0, len(sells_liv4)):
                arraynames_liv4.append(names_liv4[i].text)
            images_liv4 = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
            for r in range(len(images_liv4)):
                link = images_liv4[r].get_attribute('src')
                arraylinks_liv4.append(link)
            try:
                for testo in arraylinks_liv4:
                    livello = testo.split("_")[2].split("N")[1]
                    arraylevels_liv4.append(int(livello))
            except:
                arraylinks_liv4 = []
                arraylevels_liv4 = []
                elements = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
                elements[len(elements) - 1].click()
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA))
                cancella_elemento = self.driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA)
                cancella_elemento.click()
                images_liv4 = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
                for r in range(len(images_liv4)):
                    link = images_liv4[r].get_attribute('src')
                    arraylinks_liv4.append(link)
                for testo in arraylinks_liv4:
                    livello = testo.split("_")[2].split("N")[1]
                    arraylevels_liv4.append(int(livello))
            print(arraylevels_liv4)
            contatore_liv4 = 0
            index_liv4 = 0
            for i in range(len(arraylevels_liv4)):
                if arraylevels_liv4[i] == 4:
                    contatore_liv4 += 1
                    index_liv4 = i
                    break
                elif arraylevels_liv4[i] == 3:
                    contatore_liv4 += 1
                    index_liv4 = i
                    liv3 = True
                    break
                elif arraylevels_liv4[i] == 2:
                    contatore_liv4 += 1
                    index_liv4 = i
                    liv2 = True
                    break
                elif arraylevels_liv4[i] == 1:
                    contatore_liv4 += 1
                    index_liv4 = i
                    liv1 = True
                    break
            if contatore_liv4 == 0:
                break
            if liv1 and Clintz < 1000:
                print("Non mi bastano i clintz")
                break
            if liv2 and Clintz < 3000:
                print("Non mi bastano i clintz")
                break
            if liv3 and Clintz < 6000:
                print("Non mi bastano i clintz")
                break
            if not (liv1 or liv2 or liv3) and Clintz < 10000:
                print("Non mi bastano i clintz")
                break
            nome_carta_upgrade = arraynames_liv4[index_liv4]
            upgrades_liv4[index_liv4].click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.UPGRADE_CONFERMA_BOTTONE))
            upgrade_conferma_liv4 = self.driver.find_element(*CollezioneLocators.UPGRADE_CONFERMA_BOTTONE)
            self.driver.execute_script("arguments[0].click();", upgrade_conferma_liv4)
            rimpiazzo_liv1 = arraylinks_liv4[index_liv4].replace('_N1_', '_N2_')
            rimpiazzo_liv2 = arraylinks_liv4[index_liv4].replace('_N2_', '_N3_')
            rimpiazzo_liv3 = arraylinks_liv4[index_liv4].replace('_N3_', '_N4_')
            rimpiazzo_liv4 = arraylinks_liv4[index_liv4].replace('_N4_', '_N5_')
            if liv1:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzo_liv1 + '\"]'))
                Punti_Esperienza += 20
                Clintz -= 1000
            if liv2:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzo_liv2 + '\"]'))
                Punti_Esperienza += 30
                Clintz -= 3000
            if liv3:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzo_liv3 + '\"]'))
                Punti_Esperienza += 40
                Clintz -= 6000
            else:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzo_liv4 + '\"]'))
                Punti_Esperienza += 50
                Clintz -= 10000
            livello_evoluzione = Esperienza()
            Clintz += 2000 * (livello_evoluzione - livello_inizio)
            if Punti_Esperienza >= 1005:
                kosnikai = True
                Puoi_Vendere = True
                print("Io mi fermo qui!")
                break
        print(Punti_Esperienza)
        print(Clintz)


    def Vendi_Tutto(self):
        global Clintz
        global Punti_Esperienza
        global kosnikai
        global Puoi_Vendere
        asinfosda = True
        print(kosnikai)
        while asinfosda and not kosnikai:
            livello_inizio = Esperienza()
            arraynames = []
            arraylinks = []
            arraylevels = []
            sells = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
            names = self.driver.find_elements(*CollezioneLocators.NOMI_CARTE)
            for i in range(0, len(sells)):
                arraynames.append(names[i].text)
            images = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
            for r in range(len(images)):
                link = images[r].get_attribute('src')
                arraylinks.append(link)
            print(arraylinks)
            try:
                for testo in arraylinks:
                    nome = testo.split("_")[1]
                    arraylevels.append(nome)
            except:
                arraylinks = []
                arraylevels = []
                elements = self.driver.find_elements(*CollezioneLocators.VENDITA_BOTTONE)
                elements[len(elements) - 1].click()
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA))
                cancella_elemento = self.driver.find_element(*CollezioneLocators.CANCELLA_BOTTONE_CONFERMA)
                cancella_elemento.click()
                images = self.driver.find_elements(*CollezioneLocators.IMMAGINI_CARTE)
                for r in range(len(images)):
                    link = images[r].get_attribute('src')
                    arraylinks.append(link)
                for testo in arraylinks:
                    nome = testo.split("_")[1]
                    arraylevels.append(nome)
            print(arraylevels)
            contatore = 0
            index = 0
            for i in range(len(arraylevels)):
                if arraylevels[i] != "ENIGMA" and arraylevels[i] != "GRIFFONMOR" and arraylevels[i] != "KATE" and arraylevels[i] != "MEMENTO" and arraylevels[i] != "NADIA" and arraylevels[i] != "MISS DENNA":
                    contatore += 1
                    index = i
                    break
            if contatore == 0:
                break
            sells[index].click()
            try:
                comune = self.driver.find_element(*CollezioneLocators.COMUNE_BOTTONE)
                print("comune")
            except:
                comune = False
            try:
                non_comune = self.driver.find_element(*CollezioneLocators.NON_COMUNE_BOTTONE)
                print("non comune")
            except:
                non_comune = False
            try:
                rara = self.driver.find_element(*CollezioneLocators.RARA_BOTTONE)
                print("rara")
            except:
                rara = False
            if comune or non_comune or rara:
                if comune:
                    comune.click()
                    print("sono qui")
                    Clintz += 250
                    Punti_Esperienza += 10
                elif non_comune:
                    print("sono qui ma non comune")
                    non_comune.click()
                    Clintz += 2500
                    Punti_Esperienza += 50
                else:
                    print("rara ma qui")
                    rara.click()
                    Clintz += 9000
                    Punti_Esperienza += 100
                livello_vendita = Esperienza()
                Clintz += 2000 * (livello_vendita - livello_inizio)
                elemento_conferma = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
                print("ok3")
                elemento_conferma.click()
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + arraylinks[index] + '\"]') == [])
            if Punti_Esperienza >= 1005:
                print("Io mi fermo")
                Puoi_Vendere = True
                break
        print(Punti_Esperienza)
        print(Clintz)

    def Controlla_Cosa_Vendere(self):
        global Puoi_Vendere
        global Memento
        global Enigma
        global Kate
        global Griffonmor
        global Nadia
        global Miss_Denna
        if Puoi_Vendere:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_elements(*CollezioneLocators.NOMI_CARTE) != [])
            names = self.driver.find_elements(*CollezioneLocators.NOMI_CARTE)
            for i in range(len(names)):
                if names[i].text == "Enigma":
                    Enigma = True
                    print("Enigma dice il vero")
                elif names[i].text == "Kate":
                    Kate = True
                    print("Kate dice il vero")
                elif names[i].text == "Griffonmor":
                    Griffonmor = True
                    print("Griffonmor dice il vero")
                elif names[i].text == "Memento":
                    Memento = True
                    print("Memento dice il vero")
                elif names[i].text == "Nadia":
                    Nadia = True
                    print("Nadia dice il vero")
                elif names[i].text == "Miss Denna":
                    Miss_Denna = True
                    print("Miss Denna dice il vero")

class Mercato(BasePage):
    search_text_element = SearchTextElement()

    '''def Vendita_Vansaar(self):
        global Vansaar
        if Vansaar:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.MERCATO_BOTTONE))
            mercato = self.driver.find_element(*MercatoLocators.MERCATO_BOTTONE)
            mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE))
            il_mercato = self.driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE)
            il_mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.RICERCA_BOTTONE))
            ricerca = self.driver.find_element(*MercatoLocators.RICERCA_BOTTONE)
            ricerca.click()
            ricerca.send_keys('Vansaar')
            ricerca.send_keys(Keys.RETURN)
            try:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Vansaar")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_1).text
            except:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Vansaar")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_2).text
            valore_ = card_value.split(" ")
            valuer = ""
            for i in range(len(valore_)):
                valuer = valuer + valore_[i]
            valuer = int(valuer)
            print(valuer)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.RICERCA_BOTTONE))
            element = self.driver.find_element(*CollezioneLocators.RICERCA_BOTTONE)
            element.click()
            element.send_keys("Vansaar")
            element.send_keys(Keys.RETURN)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA))
            element = self.driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.CAMPO_CLINTZ))
            element = self.driver.find_element(*CollezioneLocators.CAMPO_CLINTZ)
            element.click()
            element.send_keys(valuer - 10)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA))
            element = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
            element.click()
            print("Finito")'''

    def Vendita_Enigma(self):
        global Enigma
        if Enigma:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.MERCATO_BOTTONE))
            mercato = self.driver.find_element(*MercatoLocators.MERCATO_BOTTONE)
            mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE))
            il_mercato = self.driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE)
            il_mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.RICERCA_BOTTONE))
            ricerca = self.driver.find_element(*MercatoLocators.RICERCA_BOTTONE)
            ricerca.click()
            ricerca.send_keys('Enigma')
            ricerca.send_keys(Keys.RETURN)
            try:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Enigma")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_1).text
            except:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Enigma")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_2).text
            valore_ = card_value.split(" ")
            valuer = ""
            for i in range(len(valore_)):
                valuer = valuer + valore_[i]
            valuer = int(valuer)
            print(valuer)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.RICERCA_BOTTONE))
            element = self.driver.find_element(*CollezioneLocators.RICERCA_BOTTONE)
            element.click()
            element.send_keys("Enigma")
            element.send_keys(Keys.RETURN)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA))
            element = self.driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.CAMPO_CLINTZ))
            element = self.driver.find_element(*CollezioneLocators.CAMPO_CLINTZ)
            element.click()
            element.send_keys(valuer - 10)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA))
            element = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
            element.click()
            print("Finito")

    def Vendita_Griffonmor(self):
        global Griffonmor
        if Griffonmor:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.MERCATO_BOTTONE))
            mercato = self.driver.find_element(*MercatoLocators.MERCATO_BOTTONE)
            mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE))
            il_mercato = self.driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE)
            il_mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.RICERCA_BOTTONE))
            ricerca = self.driver.find_element(*MercatoLocators.RICERCA_BOTTONE)
            ricerca.click()
            ricerca.send_keys('Griffonmor')
            ricerca.send_keys(Keys.RETURN)
            try:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Griffonmor")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_1).text
            except:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Griffonmor")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_2).text
            valore_ = card_value.split(" ")
            valuer = ""
            for i in range(len(valore_)):
                valuer = valuer + valore_[i]
            valuer = int(valuer)
            print(valuer)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.RICERCA_BOTTONE))
            element = self.driver.find_element(*CollezioneLocators.RICERCA_BOTTONE)
            element.click()
            element.send_keys("Griffonmor")
            element.send_keys(Keys.RETURN)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA))
            element = self.driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.CAMPO_CLINTZ))
            element = self.driver.find_element(*CollezioneLocators.CAMPO_CLINTZ)
            element.click()
            element.send_keys(valuer - 10)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA))
            element = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
            element.click()
            print("Finito")

    def Vendita_Kate(self):
        global Kate
        if Kate:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.MERCATO_BOTTONE))
            mercato = self.driver.find_element(*MercatoLocators.MERCATO_BOTTONE)
            mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE))
            il_mercato = self.driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE)
            il_mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.RICERCA_BOTTONE))
            ricerca = self.driver.find_element(*MercatoLocators.RICERCA_BOTTONE)
            ricerca.click()
            ricerca.send_keys('Kate')
            ricerca.send_keys(Keys.RETURN)
            try:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Kate")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_1).text
            except:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Kate")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_2).text
            valore_ = card_value.split(" ")
            valuer = ""
            for i in range(len(valore_)):
                valuer = valuer + valore_[i]
            valuer = int(valuer)
            print(valuer)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.RICERCA_BOTTONE))
            element = self.driver.find_element(*CollezioneLocators.RICERCA_BOTTONE)
            element.click()
            element.send_keys("Kate")
            element.send_keys(Keys.RETURN)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA))
            element = self.driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.CAMPO_CLINTZ))
            element = self.driver.find_element(*CollezioneLocators.CAMPO_CLINTZ)
            element.click()
            element.send_keys(valuer - 10)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA))
            element = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
            element.click()
            print("Finito")

    def Vendita_Memento(self):
        global Memento
        if Memento:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.MERCATO_BOTTONE))
            mercato = self.driver.find_element(*MercatoLocators.MERCATO_BOTTONE)
            mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE))
            il_mercato = self.driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE)
            il_mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.RICERCA_BOTTONE))
            ricerca = self.driver.find_element(*MercatoLocators.RICERCA_BOTTONE)
            ricerca.click()
            ricerca.send_keys('Memento')
            ricerca.send_keys(Keys.RETURN)
            try:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Memento")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_1).text
            except:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Memento")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_2).text
            valore_ = card_value.split(" ")
            valuer = ""
            for i in range(len(valore_)):
                valuer = valuer + valore_[i]
            valuer = int(valuer)
            print(valuer)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.RICERCA_BOTTONE))
            element = self.driver.find_element(*CollezioneLocators.RICERCA_BOTTONE)
            element.click()
            element.send_keys("Memento")
            element.send_keys(Keys.RETURN)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA))
            element = self.driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.CAMPO_CLINTZ))
            element = self.driver.find_element(*CollezioneLocators.CAMPO_CLINTZ)
            element.click()
            element.send_keys(valuer - 10)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA))
            element = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
            element.click()
            print("Finito")

    def Vendita_Miss_Denna(self):
        global Miss_Denna
        if Miss_Denna:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.MERCATO_BOTTONE))
            mercato = self.driver.find_element(*MercatoLocators.MERCATO_BOTTONE)
            mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE))
            il_mercato = self.driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE)
            il_mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.RICERCA_BOTTONE))
            ricerca = self.driver.find_element(*MercatoLocators.RICERCA_BOTTONE)
            ricerca.click()
            ricerca.send_keys('Miss Denna')
            ricerca.send_keys(Keys.RETURN)
            try:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Miss Denna")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_1).text
            except:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Miss Denna")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_2).text
            valore_ = card_value.split(" ")
            valuer = ""
            for i in range(len(valore_)):
                valuer = valuer + valore_[i]
            valuer = int(valuer)
            print(valuer)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.RICERCA_BOTTONE))
            element = self.driver.find_element(*CollezioneLocators.RICERCA_BOTTONE)
            element.click()
            element.send_keys("Miss Denna")
            element.send_keys(Keys.RETURN)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA))
            element = self.driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.CAMPO_CLINTZ))
            element = self.driver.find_element(*CollezioneLocators.CAMPO_CLINTZ)
            element.click()
            element.send_keys(valuer - 10)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA))
            element = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
            element.click()
            print("Finito")

    def Vendita_Nadia(self):
        global Memento
        if Memento:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.MERCATO_BOTTONE))
            mercato = self.driver.find_element(*MercatoLocators.MERCATO_BOTTONE)
            mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE))
            il_mercato = self.driver.find_element(*MercatoLocators.IL_MERCATO_BOTTONE)
            il_mercato.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MercatoLocators.RICERCA_BOTTONE))
            ricerca = self.driver.find_element(*MercatoLocators.RICERCA_BOTTONE)
            ricerca.click()
            ricerca.send_keys('Nadia')
            ricerca.send_keys(Keys.RETURN)
            try:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Nadia")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_1).text
            except:
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*MercatoLocators.NOME_CARTA).text == "Nadia")
                card_value = self.driver.find_element(*MercatoLocators.VALORE_CARTA_2).text
            valore_ = card_value.split(" ")
            valuer = ""
            for i in range(len(valore_)):
                valuer = valuer + valore_[i]
            valuer = int(valuer)
            print(valuer)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE))
            element = self.driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.RICERCA_BOTTONE))
            element = self.driver.find_element(*CollezioneLocators.RICERCA_BOTTONE)
            element.click()
            element.send_keys("Nadia")
            element.send_keys(Keys.RETURN)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA))
            element = self.driver.find_element(*CollezioneLocators.ALTRO_BOTTONE_VENDITA)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.CAMPO_CLINTZ))
            element = self.driver.find_element(*CollezioneLocators.CAMPO_CLINTZ)
            element.click()
            element.send_keys(valuer - 10)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA))
            element = self.driver.find_element(*CollezioneLocators.VENDITA_BOTTONE_CONFERMA)
            element.click()
            print("Finito")



class Negozio(BasePage):
    search_text_element = SearchTextElement()

    def Pacchetto_(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*NegozioLocators.PACCHETTO_BOTTONE))
        element = self.driver.find_element(*NegozioLocators.PACCHETTO_BOTTONE)
        element.click()

    def Paradox_Choose(self):
        loop = True
        while loop:
            try:
                time.sleep(2)
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(*NegozioLocators.PARADOX_BOTTONE))
                element = self.driver.find_element(*NegozioLocators.PARADOX_BOTTONE)
                element.click()
                break
            except:
                time.sleep(1)



    def Skeelz_Choose(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*NegozioLocators.SKEELZ_BOTTONE))
        element =  self.driver.find_element(*NegozioLocators.SKEELZ_BOTTONE)
        element.click()

    def Dominion_Choose(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*NegozioLocators.DOMINION_BOTTONE))
        element = self.driver.find_element(*NegozioLocators.DOMINION_BOTTONE)
        element.click()

    def Komboka_Choose(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*NegozioLocators.KOMBOKA_BOTTONE))
        element = self.driver.find_element(*NegozioLocators.KOMBOKA_BOTTONE)
        element.click()

    def Pussycats_Choose(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*NegozioLocators.PUSSYCATS_BOTTONE))
        element = self.driver.find_element(*NegozioLocators.PUSSYCATS_BOTTONE)
        element.click()

    def Berzerk_Choose(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*NegozioLocators.BERZERK_BOTTONE))
        element = self.driver.find_element(*NegozioLocators.BERZERK_BOTTONE)
        element.click()

    def Acquista_Pacchetto(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*NegozioLocators.ACQUISTA_BOTTONE))
        element = self.driver.find_element(*NegozioLocators.ACQUISTA_BOTTONE)
        element.click()

    def Flip_All_Check(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PacchettoLocators.FLIP_ALL_BOTTONE))


class Pacchetto(BasePage):
    search_text_element = SearchTextElement()

    def Flip_All(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PacchettoLocators.FLIP_ALL_BOTTONE))
        element = self.driver.find_element(*PacchettoLocators.FLIP_ALL_BOTTONE)
        element.click()

    def Pack_Value(self):
        global count
        global Money
        Money = False
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PacchettoLocators.CLINTZ_TESTO_COMPLETO).text != "")
        elemento = self.driver.find_element(*PacchettoLocators.CLINTZ_TESTO).text.split(" ")
        elemento.remove("Clintz")
        Value = ""
        for i in range(len(elemento)):
            Value = Value + elemento[i]
        Value = int(Value)
        print(Value)
        if Value > 20000000:
            f = open("il_mio_file","a")
            f.write(values.mail_string1 + str(count - 1) + values.mail_string2 +": " + str(Value) +"\n")
            f.close()
            #winsound.PlaySound("Tadaaa.wav", winsound.SND_ASYNC)
            Money = True

    def Moneta(self):
        global Money
        if Money:
            return True
        return False

    def Collezione_(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE))
        element = self.driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE)
        element.click()

    def La_Mia_Collezione(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE))
        element = self.driver.find_element(*GiocaLocators.LA_MIA_COLLEZIONE_BOTTONE)
        element.click()

    def Biografia_(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PacchettoLocators.BIOGRAFIA_BOTTONE))
        element = self.driver.find_element(*PacchettoLocators.BIOGRAFIA_BOTTONE)
        self.driver.execute_script("arguments[0].click();", element)

    def Disconnessione_Check(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*BiografiaLocators.DISCONNESSIONE_BOTTONE))

class Biografia(BasePage):
    search_text_element = SearchTextElement()

    def Disconnessione(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*BiografiaLocators.DISCONNESSIONE_BOTTONE))
        element = self.driver.find_element(*BiografiaLocators.DISCONNESSIONE_BOTTONE)
        element.click()

    def Disconnessione_Conferma(self):
        element = self.driver.find_element(*CollezioneLocators.UPGRADE_CONFERMA_BOTTONE)
        element.click()


    def Identificazione_Check(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*PaginaInizialeLocators.IDENTIFICATI_BOTTONE))

class Pagina_Email(BasePage):
    search_text_element = SearchTextElement()
    global Puoi_Vendere

    def Creazione_Mail(self):
        global count
        Nomsa = True
        self.driver.execute_script("window.open('http://www.yopmail.com/it/')")
        finestra_mail = self.driver.window_handles[1]
        finestra_urban = self.driver.window_handles[0]
        self.driver.switch_to.window(finestra_mail)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*EmailLocators.MAIL_BUTTON))
        element = self.driver.find_element(*EmailLocators.MAIL_BUTTON)
        element.click()
        element.clear()
        element.send_keys(values.mail_string1 + str(count - 1))
        element = self.driver.find_element(*EmailLocators.INVIO_BOTTONE)
        element.click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*EmailLocators.AGGIORNAMENTO_MAIL_BOTTONE))
        while Nomsa:
            element = self.driver.find_element(*EmailLocators.AGGIORNAMENTO_MAIL_BOTTONE)
            element.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*EmailLocators.NUMERO_MAIL))
            time.sleep(2)
            try:
                numero_mail = self.driver.find_element(*EmailLocators.NUMERO_MAIL).text.split(" ")[0]
                numero_mail = int(numero_mail)
                if numero_mail > 0:
                    break
            except:
                pass
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*EmailLocators.IFRAME))
        iframe = self.driver.find_element(*EmailLocators.IFRAME)
        self.driver.switch_to.frame(iframe)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*EmailLocators.LINK_CONFERMA))
        conferma_email = self.driver.find_element(*EmailLocators.LINK_CONFERMA)
        conferma_email.click()
        try:
            self.driver.switch_to.window(self.driver.window_handles[2])
        except:
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[2])
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*EmailLocators.MESSAGGIO_SUCCESSO))
        self.driver.close()
        self.driver.switch_to.window(finestra_mail)
        self.driver.close()
        self.driver.switch_to.window(finestra_urban)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*GiocaLocators.COLLEZIONE_BOTTONE))

class SearchResultsPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source