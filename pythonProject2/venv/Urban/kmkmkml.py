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

array = []
PATH = "C:\Program Files (x86)\chromedriver.exe"
ignored_exceptions = [StaleElementReferenceException, NoSuchElementException]
chromeOptions = Options()
chromeOptions.headless = False
prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
driver.get("https://10fastfingers.com/advanced-typing-test/italian")
WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath('//*[@id="inputfield"]'))

for i in range(1, 20):
    WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath('//*[@id="row1"]/span[' + str(i) + ']'))
    elemento = driver.find_element_by_xpath('//*[@id="row1"]/span[' + str(i) + ']').text
    array.append(elemento)
    print(elemento)
    elemento = ""
element = driver.find_element_by_xpath('//*[@id="inputfield"]')
for i in range(20):
    element.send_keys(array[i])
    element.send_keys(Keys.SPACE)
