import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
import winsound
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

vocabolario = {"Kate": 1966, "Enigma": 1993, "Death Adder": 1760, "Kiki Cr": 209, "Dragan Mt": 315, "Dj Korr Mt": 223, "Scarlett Mt": 277, "Manon Mt": 276, "General Mt": 219, "Cannibal Jo Mt": 1595, "Lyse Teria Mt": 189, "Smokey Mt": 516, "Kerozinn Mt": 382, "Guru Cr": 229, "Sigmund Mt": 241, "Nemo Mt": 1701, "Ymirah Mt": 1486, "Pandemos Cr": 2047, "Tanaereva Mt": 224, "Quetzal Mt": 1577, "Dounia Mt": 1220, "ED-0": 2065, "Elya Cr": 361, "Memento": 1885, "Robert Cobb": 1715, "Griffonmor": 2014, "Volkan Cr": 1872, "Jackie Cr": 182, "Alec Mt": 445, "Lady Ametia Cr": 1934, "Splata Cr": 385, "Lamar Cr": 313, "Host 254": 2075, "Host 516": 2074, 'Advisor 259': 2084, 'Advisor 1767': 2085}
lista = ["Kate", "Enigma", "Death Adder", "Kiki Cr", "Dragan Mt", "Dj Korr Mt", "Scarlett Mt", "Manon Mt", "General Mt", "Cannibal Jo Mt", "Lyse Teria Mt", "Smokey Mt", "Kerozinn Mt", "Guru Cr", "Sigmund Mt", "Nemo Mt", "Ymirah Mt", "Pandemos Cr", "Tanaereva Mt", "Quetzal Mt", "Dounia Mt", "ED-0", "Elya Cr", "Memento", "Robert Cobb", "Griffonmor", "Volkan Cr", "Jackie Cr", "Alec Mt", "Lady Ametia Cr", "Splata Cr", "Lamar Cr", "Host 254", "Host 516", 'Advisor 259', 'Advisor 1767']

f = open('Convertitore txt', "r")
e = open('Convertitore txt', "r")
array = []
array2 = []
array3 = []
array4 = []
array5 = []
x = 0
k = False
def definisci():
    global k
    global array
    global array2
    global array3
    global array4
    global array5
    for i in range(len(f.readlines())):
        array.append(e.readline())
    if len(array) > 1:
        k = True


        class Profili:
            def __init__(self, nome, valore, prezzo):
                self.nome = nome
                self.valore = valore
                self.prezzo = prezzo

            def ritornavalore(self):
                return self.valore

            def ritornanome(self):
                return self.nome

            def ritornaprezzo(self):
                return self.prezzo


        for i in range(len(array)):
            profilo = Profili(array[i].split(':')[0], array[i].split(': ')[1].split(' -->')[0],
                              array[i].split(': ')[1].split(' --> ')[1].split('\n')[0].split(' (')[0])
            array2.append(profilo)
        for i in range(len(array2)):
            array3.append((array2[i].nome))
        for i in range(len(array2)):
            array4.append(int(array2[i].valore))
        for i in range(len(array2)):
            array5.append(float(array2[i].prezzo))
def converti(valore):
    a = 0
    prezzo = 0
    for i in range(1, valore + 1):
        if i <= 1000:
            a += 1 / 50
        else:
            a += 1 / 120
        b = 1 / (80 + a)
        prezzo = round(i * b) - 0.01
    return prezzo

def Faccio_Tutto_Io():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    ignored_exceptions = [StaleElementReferenceException, NoSuchElementException]
    chromeOptions = Options()
    chromeOptions.headless = True
    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
    driver.get('https://iclintz.com/characters/card.php?ID=900')
    try:
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[1]/div/a'))
        driver.find_element_by_xpath('/html/body/div[1]/div/a').click()
    except:
        pass

    def ricalcolo_ValoreAttualeCarta():
        global lista
        global vocabolario
        global k
        global array3
        global array4
        global array5
        for i in range(len(lista)):
            driver.get('https://iclintz.com/characters/card.php?ID=' + str(vocabolario[lista[i]]))
            WebDriverWait(driver, 10).until(
                                lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]'))
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]').click()
            WebDriverWait(driver, 10).until(
                                lambda driver: driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]'))
            elemento = driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]').text.split(" ")
            Value = ""
            for l in range(len(elemento)):
                Value = Value + elemento[l]
            Value = int(Value)
            Value = round(Value/1000000)
            if k:
                if int(round(converti(Value) - array5[i])) > 0:
                    print(lista[i] + ': ' + str(Value) + ' --> ' + str(converti(Value)) + ' (+' + str(int(round(converti(Value) - array5[i]))) +')')
                    a.write(lista[i] + ': ' + str(Value) + ' --> ' + str(converti(Value)) + ' (+' + str(int(round(converti(Value) - array5[i]))) +')' + '\n')
                elif int(round(converti(Value) - array5[i])) < 0:
                    print(lista[i] + ': ' + str(Value) + ' --> ' + str(converti(Value)) + ' (' + str(int(round(converti(Value) - array5[i]))) +')')
                    a.write(lista[i] + ': ' + str(Value) + ' --> ' + str(converti(Value)) + ' (' + str(int(round(converti(Value) - array5[i]))) +')' + '\n')
                else:
                    print(lista[i] + ': ' + str(Value) + ' --> ' + str(converti(Value)))
                    a.write(lista[i] + ': ' + str(Value) + ' --> ' + str(converti(Value)) + '\n')
            else:
                print(lista[i] + ': ' + str(Value) + ' --> ' + str(converti(Value)))
                a.write(lista[i] + ': ' + str(Value) + ' --> ' + str(converti(Value)) +'\n')

    return ricalcolo_ValoreAttualeCarta()

argo = input('Vuoi andare online? ')

if argo == "S" or argo == "s":
    definisci()
    a = open('Convertitore txt', 'w')
    Faccio_Tutto_Io()
    a.close()
else:
    n = int(input('Inserisci il numero delle carte da valutare: '))
    for i in range(n):
        print(converti(int(input("Inserisci il valore: "))))
    if n == 0:
        z = input("Vuoi usare il convertitore? ")
        if z == "S" or z == "s":
            def converti():
                a = 0
                for i in range(1, 2201):
                    if i <= 1000:
                        a += 1 / 50
                    else:
                        a += 1 / 120
                    b = 1 / (80 + a)
                    prezzo = i * b
                    print(str(prezzo) + ' per i = ' + str(i))

            converti()


