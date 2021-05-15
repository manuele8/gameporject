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
PATH = "C:\Program Files (x86)\chromedriver.exe"
ignored_exceptions = [StaleElementReferenceException, NoSuchElementException]
chromeOptions = Options()
chromeOptions.headless = True
prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
driver.get("https://iclintz.com/characters/card.php?ID=1885")
try:
    WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath('/html/body/div[1]/div/a'))
    driver.find_element_by_xpath('/html/body/div[1]/div/a').click()
except:
    pass
WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]'))
driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[6]/ul/li[2]').click()
WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]'))
elemento = driver.find_element_by_xpath('//*[@id="tab_2"]/div/div/table/tbody/tr[1]/td[3]').text.split(" ")
Value = ""
Valore_Attuale_Memento = 0
for i in range(len(elemento)):
    Value = Value + elemento[i]
Value = int(Value)
Value = Value/1000000
Valore_Attuale_Memento = Value
print(Valore_Attuale_Memento)
time.sleep(300)
bonsai = True
while bonsai:
    driver.refresh()
    try:
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[1]/div/a'))
        driver.find_element_by_xpath('/html/body/div[1]/div/a').click()
    except:
        pass
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
    Value = Value / 1000000
    if Valore_Attuale_Memento < Value:
        bonsai = False
        print("La tua carta è stata venduta")
    else:
        print("Non ancora", "(" + str(Value) + ")")
        time.sleep(300)

