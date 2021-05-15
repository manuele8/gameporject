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
chromeOptions.headless = False
prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
driver.get('https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2Fdp%2FB08KJF2D25%2Fref%3Dnav_ya_signin%3Fpf_rd_p%3D07b25a9a-1f5d-4493-96dd-716b3478304c%26pf_rd_r%3DGG5HT4D1RQ0AQC42SCES%26pd_rd_wg%3DSlQxU%26pd_rd_w%3DVWzfs%26qid%3D1609411593%26pd_rd_r%3D48bcd2b7-e728-4406-a4d1-569f5d997d14&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
WebDriverWait(driver, 15).until(
    lambda driver: driver.find_element_by_xpath('//*[@id="ap_email"]'))
element = driver.find_element_by_xpath('//*[@id="ap_email"]')
element.clear()
element.send_keys('matteo.pedicillo0805@gmail.com')
WebDriverWait(driver, 15).until(
    lambda driver: driver.find_element_by_xpath('//*[@id="continue"]'))
element = driver.find_element_by_xpath('//*[@id="continue"]')
element.click()
WebDriverWait(driver, 15).until(
    lambda driver: driver.find_element_by_xpath('//*[@id="ap_password"]'))
element = driver.find_element_by_xpath('//*[@id="ap_password"]')
element.clear()
element.send_keys('Tunon613noo')
WebDriverWait(driver, 15).until(
    lambda driver: driver.find_element_by_xpath('//*[@id="signInSubmit"]'))
element = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
element.click()
time.sleep(5)
driver.execute_script("window.open('https://www.amazon.it/dp/B08KKJ37F7/ref=sxts_spkl_2_1_07b25a9a-1f5d-4493-96dd-716b3478304c?pf_rd_p=07b25a9a-1f5d-4493-96dd-716b3478304c&pf_rd_r=HCRPD3NA7JCWW72AEWCA&pd_rd_wg=GB0Zz&pd_rd_w=NQMHv&qid=1609420848&pd_rd_r=823059e8-d38f-46b3-b974-db1d818996d9')")
play_standard = driver.window_handles[1]
play_digital = driver.window_handles[0]
driver.switch_to.window(play_digital)
vocabolario = {0: play_digital, 1: play_standard}
i = 0
while True:
    try:
        WebDriverWait(driver, 6).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="buy-now-button"]'))
        element = driver.find_element_by_xpath('//*[@id="buy-now-button"]')
        element.click()
        print(0)
        break
    except:
        print(1)
        if i == 1:
            i = 0
        else:
            i = 1
        driver.switch_to.window(vocabolario[i])
        driver.refresh()

WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span'))
element = driver.find_element_by_xpath('//*[@id="subtotals-marketplace-spp-bottom"]/span')
print(element.text)
x = float(element.text.split('Totale ordine:')[1].split(' €')[0].split(',')[0])
y = float(element.text.split('Totale ordine:')[1].split(' €')[0].split(',')[1])
z = x + y/100
print(z)
if (z <= 400 and z >= 399) or (z <= 500 and z >= 499):
    WebDriverWait(driver, 15).until(
        lambda driver: driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input'))
    element = driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
    element.click()
else:
    print("Non posso")
time.sleep(300)

