# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
path = r'C:\Users\Manu\Desktop\Tutto\App'
PATH = path + r'\\chromedriver.exe'
ignored_exceptions=[StaleElementReferenceException, NoSuchElementException]
chromeOptions = Options()
chromeOptions.headless = False

array = []
array2 = ['🎶 Mi True Wireless Earbuds Air2 SE, Auricolare In-Ear ENC Smart Wireless Bluetooth 5.0\n\n‼️ Minimo Storico ‼️\n💰 A soli 14,99€ invece di 16,99€\n\n👉 https://amzn.to/3ieSW0y', '🖨 Stampante Multifunzione HP OfficeJet 8012e - 6 mesi di inchiostro inclusi con HP+\n\n‼️ Minimo Storico ‼️\n💰 A soli 99,99€ invece di 139,00€\n\n👉 https://amzn.to/3l2nHZV', '🍻 Peroni Cruda Birra - Cassa da 24 Bottiglie da 33cl, Non Pastorizzata - 7920 ml\n\n💰 A soli 20,20€ invece di 23,76€\n\n👉 https://amzn.to/3zmwI3K\n\nPerfetta per rinfrescarvi in estate 🔝', '🍻 Nastro Azzurro Birra Analcolica- Cassa da 24 x 33 cl (7.92 l)\n\n‼️ Minimo Storico ‼️\n💰 A soli 19,38€ invece di 23,92€\n\n👉 https://amzn.to/36Yst20', '💻 2021 Apple iPad Pro (12,9", Wi-Fi, 256GB) - Grigio siderale (5ª generazione)\n\n‼️ Minimo Storico ‼️\n💰 A soli 1.272,87€ invece di 1.329,00€\n\n👉 https://amzn.to/3i1sU2c\n\nMinimo per il SUPER iPad Pro con M1!', '📺 Samsung TV QE43Q64TAUXZT Serie Q60T Modello Q64T QLED Smart TV 43", con Alexa integrata, Ultra HD 4K, Wi-Fi, Silver, 2020, Esclusiva Amazon\n\n💰 A soli 339,21€ invece di 484,59€\n\n👉 https://amzn.to/3iMniYH\n\nSegnalata anche su @UsatoScontato, ottima occasione!\n\n✅ Sconto automatico visibile nel carrello in fase di pagamento 🛒', '❗️PREZZONE❗️\n🧦 Puma Sportsocken Cush Crew 6P Calzini Sportivi, Nero\n\n‼️ Minimo Storico ‼️\n💰 A soli 6,99€ invece di 15,99€\n\n👉 https://amzn.to/3ePVXUn\n\nPrezzone per ben 6 paia!', '🖥 Acer EG270Pbipx Monitor Gaming FreeSync Premium 27", Display IPS FHD\n\n‼️ Minimo Storico ‼️\n💰 A soli 176,55€ invece di 249,90€\n\n👉 https://amzn.to/3kPfqs7\n\nUn prezzo super accattivante per un 27”!', '❌ ERRORE o BOMBA? 💣\n👩 KYG Epilatore a Luce Pulsata Dispositivo IPL 500.000 Pulsazioni Utilizzo Bianco\n\n‼️ Minimo Storico ‼️\n💰 A soli 19,99€\n\n👉 https://amzn.to/3Bu4hTg', '📺 Samsung The Frame QLED 4K 2021 65LS03A Smart TV 65", Risoluzione 4K UHD\n\n‼️ Minimo Storico ‼️\n💰 A soli 1.618,99€ invece di 1.999,00€\n\n👉 https://amzn.to/2Tu2zQE\n\nUna tv MERAVIGLIOSA che arrederà il vostro salotto 😍\nPrezzo eccezionale per il 65”!', '😱 PREZZO DA URLO 😱\n💾 LaCie Mobile Drive, 2 TB, Hard Disk Esterno Portatile, USB-C, USB 3.0, Moon Silver, 2 anni di servizi Rescue (STHG2000400)\n\n💰 A soli 56,99€ invece di 134,99€\n\n👉 https://amzn.to/3BDa09m\n\n✅ Sconto automatico visibile nel carrello in fase di pagamento 🛒', '🔥 AFFARE 🔥\n🏡 Vivere UHSDO8-24 Amaca con Supporto Brasiliana, Cotone, 250 cm, Portata 200 kg Borsa da Trasporto inclu, Oasi Doppia, Oasis\n\n‼️ Minimo Storico ‼️\n💰 A soli 59,57€ invece di 158,95€\n\n👉 https://amzn.to/3zwo2rD\n\nTop per rilassarsi in queste calde giornate 😎', '👕 Lacoste Sport TH0123 T-Shirt, Marine, M Uomo\n\n💰 A soli 35,00€ invece di 45,00€\n\n👉 https://amzn.to/3zy0DWQ', '💻 HUAWEI MateBook X Pro 2021 Laptop, Display 3K FullView Touchscreen, Processore Intel i7-1165G7, 16 GB di memoria RAM, SSD da 1 TB, Intel Iris Xe Graphics, Win 10 Home, Layout Italiano, Space Gray\n\n‼️ Minimo Storico ‼️\n💰 A soli 1.489,66€ invece di 1.899,00€\n\n👉 https://amzn.to/3eRQtIG', '💣💣 BOMBA!!! 💣💣\n🎶 AUKEYPOWER Cuffie Bluetooth 5 in-ear, 28 ore di riproduzione con custodia di ricarica\n\n‼️ Minimo Storico ‼️\n💰 A soli 19,99€ invece di 39,99€\n✂️ Applica il coupon in pagina\n\n👉 https://amzn.to/3BB27kK', '🖨 Xiaomi Mi Portable Photo Printer, Stampante Laser Portatile, Carta fotografica lucida, Stampa termica, Connessione Bluetooth/USB/WLAN, Bianco, Versione Italiana\n\n💰 A soli 50,99€ invece di 69,99€\n\n👉 https://amzn.to/3x3ixPp', '📱 OnePlus 9 5G Smartphone Senza SIM con Fotocamera Hasselblad, 8 GB RAM + 128 GB, Blu (Arctic Sky)\n\n‼️ Minimo Storico ‼️\n💰 A soli 605,04€ invece di 719,00€\n\n👉 https://amzn.to/3eRVvW8', '💣💣 BOMBA!!! 💣💣\n🎒 Vans VN0A3I6R5S21 Unisex - Adulto , Marina, One Size\n\n‼️ Minimo Storico ‼️\n💰 A soli 18,95€ invece di 37,99€\n\n👉 https://amzn.to/3kN7Pu1']
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


class miamadre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
        self.driver.get("https://www.amiciapple.it/offerte/")

    def test(self):
        global array, array3, array4, array5, array6, array7, Informazioni, ultimo_elemento, Out, jk
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
                    if "💰 A soli" in elemento:
                        elementoo = (elemento.split("💰 A soli")[1].split('\n')[0])
                        if elementoo.count('€') == 1:
                            informazione.prezzosc = elementoo.split('€')[0].split(' ')[1].replace(',', '.')
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('€')[0].split(' ')[1].replace(',', '.')
                            informazione.prezzoin = elementoo.split('invece di')[1].split('€')[0].split(' ')[1].replace(',', '.')
                    elif "💰 A solo" in elemento:
                        elementoo = (elemento.split("💰 A solo")[1].split('\n')[0])
                        if elementoo.count('€') == 1:
                            informazione.prezzosc = elementoo.split('€')[0]
                        elif "invece di" in elementoo:
                            informazione.prezzosc = elementoo.split('€')[0]
                            informazione.prezzoin = elementoo.split('invece di')[1].split('€')[0]
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
            x = float(element.text.split('Totale ordine:')[1].split(' €')[0].split(',')[0])
            y = float(element.text.split('Totale ordine:')[1].split(' €')[0].split(',')[1])
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




    def tearDown(self):
        self.driver.close()




if __name__ == '__main__':
    unittest.main()

