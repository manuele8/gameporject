# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
ignored_exceptions=[StaleElementReferenceException, NoSuchElementException]
chromeOptions = Options()
chromeOptions.headless = True

array = []
array2 = ['ð¶ Mi True Wireless Earbuds Air2 SE, Auricolare In-Ear ENC Smart Wireless Bluetooth 5.0\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 14,99â¬ invece di 16,99â¬\n\nð https://amzn.to/3ieSW0y', 'ð¨ Stampante Multifunzione HP OfficeJet 8012e - 6 mesi di inchiostro inclusi con HP+\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 99,99â¬ invece di 139,00â¬\n\nð https://amzn.to/3l2nHZV', 'ð» Peroni Cruda Birra - Cassa da 24 Bottiglie da 33cl, Non Pastorizzata - 7920 ml\n\nð° A soli 20,20â¬ invece di 23,76â¬\n\nð https://amzn.to/3zmwI3K\n\nPerfetta per rinfrescarvi in estate ð', 'ð» Nastro Azzurro Birra Analcolica- Cassa da 24 x 33 cl (7.92 l)\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 19,38â¬ invece di 23,92â¬\n\nð https://amzn.to/36Yst20', 'ð» 2021 Apple iPad Pro (12,9", Wi-Fi, 256GB) - Grigio siderale (5Âª generazione)\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 1.272,87â¬ invece di 1.329,00â¬\n\nð https://amzn.to/3i1sU2c\n\nMinimo per il SUPER iPad Pro con M1!', 'ðº Samsung TV QE43Q64TAUXZT Serie Q60T Modello Q64T QLED Smart TV 43", con Alexa integrata, Ultra HD 4K, Wi-Fi, Silver, 2020, Esclusiva Amazon\n\nð° A soli 339,21â¬ invece di 484,59â¬\n\nð https://amzn.to/3iMniYH\n\nSegnalata anche su @UsatoScontato, ottima occasione!\n\nâ Sconto automatico visibile nel carrello in fase di pagamento ð', 'âï¸PREZZONEâï¸\nð§¦ Puma Sportsocken Cush Crew 6P Calzini Sportivi, Nero\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 6,99â¬ invece di 15,99â¬\n\nð https://amzn.to/3ePVXUn\n\nPrezzone per ben 6 paia!', 'ð¥ Acer EG270Pbipx Monitor Gaming FreeSync Premium 27", Display IPS FHD\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 176,55â¬ invece di 249,90â¬\n\nð https://amzn.to/3kPfqs7\n\nUn prezzo super accattivante per un 27â!', 'â ERRORE o BOMBA? ð£\nð© KYG Epilatore a Luce Pulsata Dispositivo IPL 500.000 Pulsazioni Utilizzo Bianco\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 19,99â¬\n\nð https://amzn.to/3Bu4hTg', 'ðº Samsung The Frame QLED 4K 2021 65LS03A Smart TV 65", Risoluzione 4K UHD\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 1.618,99â¬ invece di 1.999,00â¬\n\nð https://amzn.to/2Tu2zQE\n\nUna tv MERAVIGLIOSA che arrederÃ  il vostro salotto ð\nPrezzo eccezionale per il 65â!', 'ð± PREZZO DA URLO ð±\nð¾ LaCie Mobile Drive, 2 TB, Hard Disk Esterno Portatile, USB-C, USB 3.0, Moon Silver, 2 anni di servizi Rescue (STHG2000400)\n\nð° A soli 56,99â¬ invece di 134,99â¬\n\nð https://amzn.to/3BDa09m\n\nâ Sconto automatico visibile nel carrello in fase di pagamento ð', 'ð¥ AFFARE ð¥\nð¡ Vivere UHSDO8-24 Amaca con Supporto Brasiliana, Cotone, 250 cm, Portata 200 kg Borsa da Trasporto inclu, Oasi Doppia, Oasis\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 59,57â¬ invece di 158,95â¬\n\nð https://amzn.to/3zwo2rD\n\nTop per rilassarsi in queste calde giornate ð', 'ð Lacoste Sport TH0123 T-Shirt, Marine, M Uomo\n\nð° A soli 35,00â¬ invece di 45,00â¬\n\nð https://amzn.to/3zy0DWQ', 'ð» HUAWEI MateBook X Pro 2021 Laptop, Display 3K FullView Touchscreen, Processore Intel i7-1165G7, 16 GB di memoria RAM, SSD da 1 TB, Intel Iris Xe Graphics, Win 10 Home, Layout Italiano, Space Gray\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 1.489,66â¬ invece di 1.899,00â¬\n\nð https://amzn.to/3eRQtIG', 'ð£ð£ BOMBA!!! ð£ð£\nð¶ AUKEYPOWER Cuffie Bluetooth 5 in-ear, 28 ore di riproduzione con custodia di ricarica\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 19,99â¬ invece di 39,99â¬\nâï¸ Applica il coupon in pagina\n\nð https://amzn.to/3BB27kK', 'ð¨ Xiaomi Mi Portable Photo Printer, Stampante Laser Portatile, Carta fotografica lucida, Stampa termica, Connessione Bluetooth/USB/WLAN, Bianco, Versione Italiana\n\nð° A soli 50,99â¬ invece di 69,99â¬\n\nð https://amzn.to/3x3ixPp', 'ð± OnePlus 9 5G Smartphone Senza SIM con Fotocamera Hasselblad, 8 GB RAM + 128 GB, Blu (Arctic Sky)\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 605,04â¬ invece di 719,00â¬\n\nð https://amzn.to/3eRVvW8', 'ð£ð£ BOMBA!!! ð£ð£\nð Vans VN0A3I6R5S21 Unisex - Adulto , Marina, One Size\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 18,95â¬ invece di 37,99â¬\n\nð https://amzn.to/3kN7Pu1']
array3 = []
array4 = []
array5 = []
array6 = []
array7 = []
ultimo_elemento = None
out = False
jk = 0
class Informazioni:
    def __init__(self, nome, prezzosc, prezzoin, link, errprez = False):
        self.nome = nome
        self.prezzosc = prezzosc
        self.prezzoin = prezzoin
        self.link = link
        self.errprez = errprez

import unittest
class miamadre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
        self.driver.get("https://www.amiciapple.it/offerte/")

    def test(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
        '''   "//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))'''
        '''WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[@class='tgme_widget_message_service_date']"))
        elements = self.driver.find_elements_by_xpath("//div[@class='tgme_widget_message_service_date']")
        for element in elements:
            array.append(element.text)
        print(array)'''
        '''WebDriverWait(self.driver, 10).until(lambda driver: driver.find_elements_by_xpath("//a[@href]") != [])
        elems = self.driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            if "https://amzn.to/" in elem.get_attribute("href"):
                print(elem.get_attribute("href"))'''


    def test2(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
    def test3(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
    def test4(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
    def test5(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
    def test6(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
    def test7(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
    def test8(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
    def test9(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
    def test10(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
    def test11(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
    def test12(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)
    def test13(self):
        global array
        global array3
        global array4
        global array5
        global array6
        global array7
        global Informazioni
        global ultimo_elemento
        global Out
        global jk
        array7 = []
        array5 = []
        array4 = []
        array3 = []
        quantities = 0
        while 1:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']"))
            elem = self.driver.find_element_by_xpath("//iframe[@src='https://www.amiciapple.it/wptelegram/widget/view/@ultimoraofferte/']")
            self.driver.switch_to.frame(elem)
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]"))
            elements = self.driver.find_elements_by_xpath("//div[starts-with(@data-post, 'Ultimoraofferte/')]")
            for element in elements:
                try:
                    elemento = element.find_element_by_xpath(
                        ".//div[@class='tgme_widget_message_text js-message_text']").text
                    informazione = Informazioni(2, 3, '200', 5)
                    if "TOP" in elemento.split('\n')[0] or "BOMBA" in elemento.split('\n')[0] or "OFFERTA LAMPO" in elemento.split('\n')[0] or "PREZZONE" in \
                            elemento.split('\n')[0] or "ERRORE" in elemento.split('\n')[0] or "AFFARE" in \
                            elemento.split('\n')[0] or "PREZZO" in elemento.split('\n')[0]:
                        informazione.nome = elemento.split('\n')[1]
                    else:
                        informazione.nome = elemento.split('\n')[0]
                    if "ERRORE DI PREZZO" in elemento:
                        informazione.errprez = True
                    if "ð° A soli" in elemento:
                        elementoo = (elemento.split("ð° A soli")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0].split(' ')[1].replace(',', '.')
                    elif "ð° A solo" in elemento:
                        elementoo = (elemento.split("ð° A solo")[1].split('\n')[0])
                        if elementoo.count('â¬') == 1:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('â¬')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('â¬')[0]
                    if "https://" in elemento:
                        elementop = elemento.split('https://')[1].split('\n')[0]
                        informazione.link = 'https://' + elementop
                    array3.append(informazione)
                except:
                    pass
            for element in array3:
                    array7.append(element)
                    array4.append(element.nome)
                    array4.append(element.prezzosc)
                    array4.append(element.prezzoin)
                    array4.append(element.link)
                    array4.append(element.errprez)
                    print(array4)
                    array5.append(array4)
                    array4 = []
            print(array5)
            if jk == 0:
                print("sono qui")
                for element in array5:
                    array6.append(element)
                array5 = []
                print(array6)
            else:
                print(jk)
                print(array6)
                if array6 == array5:
                    print("False")
                    array5 = []
                else:
                    print("True")
                    array6 = []
                    for element in array5:
                        array6.append(element)
                    array5 = []
                    ultimo_elemento = array7[len(array7) - 1]
                    break
            array7 = []
            array5 = []
            array4 = []
            array3 = []
            jk += 1
            self.driver.refresh()
        quantities = int(50 / float(ultimo_elemento.prezzosc))
        if quantities > 0:
            self.driver.get(
                'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
            element.clear()
            element.send_keys('matteo.pedicillo0805@gmail.com')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
            element = self.driver.find_element_by_xpath('//*[@id="continue"]')
            element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
            element = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
            element.clear()
            element.send_keys('Tunon613no')
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
            element = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
            element.click()
            time.sleep(5)
            self.driver.get(ultimo_elemento.link)
            #time.sleep(100)
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "sp-cc-accept"]')
                element.click()
            except:
                pass
            try:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                try:
                    WebDriverWait(self.driver, 2).until(
                        lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities) + ']'))
                    element = self.driver.find_element_by_xpath(
                        '// *[ @ id = "quantity"] / option[' + str(quantities) + ']')
                    element.click()
                except:
                    for i in range(1, 100):
                        try:
                            self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element = self.driver.find_element_by_xpath(
                                '// *[ @ id = "quantity"] / option[' + str(quantities - i) + ']')
                            element.click()
                            break
                        except:
                            pass
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            except:
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "newAccordionRow"] / div / div[1] / a / i')
                element.click()
                WebDriverWait(self.driver, 6).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]'))
                element = self.driver.find_element_by_xpath('// *[ @ id = "quantity"] / option[7]')
                element.click()
                element = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
                element.click()
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
            element = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
            print(element.text)
            x = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' â¬')[0].split(',')[1])
            z = (x + y / 100) / quantities
            if z - 1 <= float(ultimo_elemento.prezzosc) and z <= 50 and float(ultimo_elemento.prezzosc) <= float(ultimo_elemento.prezzoin)/2 and z + 1 < float(ultimo_elemento.prezzoin):
                print("ok")
                WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
                element = self.driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
                element.click()
            else:
                print("not ok")
            time.sleep(20)

    def tearDown(self):
        self.driver.close()




if __name__ == '__main__':
    unittest.main()


