import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import page
import values
import time
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
import winsound
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


Valore_Attuale_Enigma = 0
Valore_Attuale_Kate = 0
Valore_Attuale_Griffonmor = 0
Valore_Attuale_Memento = 0
Valore_Attuale_Death_Adder = 0
Valore_Attuale_Nadia = 0
Valore_Attuale_Robert_Cobb = 0
Valore_Attuale_PandemosCr = 0
Valore_Attuale_ElD10S = 0

def Faccio_Tutto_Io():
    a = open('Valore Atteso', 'w')
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    ignored_exceptions = [StaleElementReferenceException, NoSuchElementException]
    chromeOptions = Options()
    chromeOptions.headless = True
    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
    driver.get("https://iclintz.com/characters/card.php?ID=1993")
    try:
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[1]/div/a'))
        driver.find_element_by_xpath('/html/body/div[1]/div/a').click()
    except:
        pass

    def ricalcolo_ValoreAttualeEnigma():
        global Valore_Attuale_Enigma
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]').click()
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]'))
        elemento = driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]').text.split(" ")
        Value = ""
        for i in range(len(elemento)):
            Value = Value + elemento[i]
        Value = int(Value)
        Value = Value/1000000
        Valore_Attuale_Enigma = Value
        a.write('Valore Attuale Enigma: ' + str(Valore_Attuale_Enigma) + '\n')
        return Valore_Attuale_Enigma

    def ricalcolo_ValoreAttualeKate():
        global Valore_Attuale_Kate
        driver.get('https://iclintz.com/characters/card.php?ID=1966')
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]').click()
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]'))
        elemento = driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]').text.split(" ")
        Value = ""
        for i in range(len(elemento)):
            Value = Value + elemento[i]
        Value = int(Value)
        Value = Value/1000000
        Valore_Attuale_Kate = Value
        a.write('Valore Attuale Kate: ' + str(Valore_Attuale_Kate) + '\n')
        return Valore_Attuale_Kate

    def ricalcolo_ValoreAttualeGriffonmor():
        global Valore_Attuale_Griffonmor
        driver.get('https://iclintz.com/characters/card.php?ID=2014')
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]').click()
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]'))
        elemento = driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]').text.split(" ")
        Value = ""
        for i in range(len(elemento)):
            Value = Value + elemento[i]
        Value = int(Value)
        Value = Value/1000000
        Valore_Attuale_Griffonmor = Value
        a.write('Valore Attuale Griffonmor: ' + str(Valore_Attuale_Griffonmor) + '\n')
        return Valore_Attuale_Griffonmor

    def ricalcolo_ValoreAttualeElD10S():
        global Valore_Attuale_ElD10S
        driver.get('https://iclintz.com/characters/card.php?ID=2056')
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]').click()
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]'))
        elemento = driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]').text.split(" ")
        Value = ""
        for i in range(len(elemento)):
            Value = Value + elemento[i]
        Value = int(Value)
        Value = Value/1000000
        Valore_Attuale_ElD10S = Value
        a.write('Valore Attuale El D10S: ' + str(Valore_Attuale_ElD10S) + '\n')
        return Valore_Attuale_ElD10S

    def ricalcolo_ValoreAttualeMemento():
        global Valore_Attuale_Memento
        driver.get('https://iclintz.com/characters/card.php?ID=1885')
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]').click()
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]'))
        elemento = driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]').text.split(" ")
        Value = ""
        for i in range(len(elemento)):
            Value = Value + elemento[i]
        Value = int(Value)
        Value = Value/1000000
        Valore_Attuale_Memento = Value
        a.write('Valore Attuale Memento: ' + str(Valore_Attuale_Memento) + '\n')
        return Valore_Attuale_Memento

    def ricalcolo_ValoreAttualeDeathAdder():
        global Valore_Attuale_Death_Adder
        driver.get('https://iclintz.com/characters/card.php?ID=1760')
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]').click()
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]'))
        elemento = driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]').text.split(" ")
        Value = ""
        for i in range(len(elemento)):
            Value = Value + elemento[i]
        Value = int(Value)
        Value = Value/1000000
        Valore_Attuale_Death_Adder = Value
        a.write('Valore Attuale Death Adder: ' + str(Valore_Attuale_Death_Adder) + '\n')
        return Valore_Attuale_Death_Adder

    def ricalcolo_ValoreAttualeNadia():
        global Valore_Attuale_Nadia
        driver.get('https://iclintz.com/characters/card.php?ID=2033')
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]').click()
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]'))
        elemento = driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]').text.split(" ")
        Value = ""
        for i in range(len(elemento)):
            Value = Value + elemento[i]
        Value = int(Value)
        Value = Value/1000000
        Valore_Attuale_Nadia = Value
        a.write('Valore Attuale Nadia: ' + str(Valore_Attuale_Nadia) + '\n')
        return Valore_Attuale_Nadia

    def ricalcolo_ValoreAttualeRobertCobb():
        global Valore_Attuale_Robert_Cobb
        driver.get('https://iclintz.com/characters/card.php?ID=1715')
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]').click()
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]'))
        elemento = driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]').text.split(" ")
        Value = ""
        for i in range(len(elemento)):
            Value = Value + elemento[i]
        Value = int(Value)
        Value = Value/1000000
        Valore_Attuale_Robert_Cobb = Value
        a.write('Valore Attuale Robert Cobb: ' + str(Valore_Attuale_Robert_Cobb) + '\n')
        return Valore_Attuale_Robert_Cobb

    def ricalcolo_ValoreAttualePandemosCr():
        global Valore_Attuale_PandemosCr
        driver.get('https://iclintz.com/characters/card.php?ID=2047')
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]').click()
        WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]'))
        elemento = driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]').text.split(" ")
        Value = ""
        for i in range(len(elemento)):
            Value = Value + elemento[i]
        Value = int(Value)
        Value = Value/1000000
        Valore_Attuale_PandemosCr = Value
        a.write('Valore Attuale Pandemos Cr: ' + str(Valore_Attuale_PandemosCr) + '\n')
        return Valore_Attuale_PandemosCr

    return ricalcolo_ValoreAttualeEnigma(), ricalcolo_ValoreAttualePandemosCr(), ricalcolo_ValoreAttualeGriffonmor(), ricalcolo_ValoreAttualeElD10S(), ricalcolo_ValoreAttualeNadia(), ricalcolo_ValoreAttualeDeathAdder(), ricalcolo_ValoreAttualeRobertCobb(), ricalcolo_ValoreAttualeMemento(), ricalcolo_ValoreAttualeKate()

