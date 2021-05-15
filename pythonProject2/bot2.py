from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import winsound
from selenium.webdriver.support.ui import WebDriverWait
'//button[@class="btn btn-primary"]'
Punti_Esperienza = 0
Clintz = 15000
array = []
array2 = []
array3 = []
vocabolario = {13: 2, 32: 3, 69: 4, 130: 5, 221: 6, 348: 7, 517: 8, 734: 9, 1005: 10}

def Esperienza():
    for i in range(len(vocabolario)-1):
        if Punti_Esperienza > list(vocabolario)[i] and Punti_Esperienza < list(vocabolario)[i+1]:
            return vocabolario[list(vocabolario)[i]]
        elif Punti_Esperienza > 1005:
            return 10

Puoi_Vendere = False
kosnikai = False
Griffonmor = False
Griffonmor = False
Kate = False
Griffonmor = False
o = 0
count = 0
c = 128379121
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.urban-rivals.com/")
time.sleep(2)
identification = driver.find_element_by_link_text("Identificati")
identification.click()
time.sleep(2)
email = driver.find_element_by_xpath('//*[@id="register"]/form/div[1]/input')
email.click()
email.send_keys("nisadjasl" + str(c) + "@yopmail.com")
password = driver.find_element_by_xpath('//*[@id="register"]/form/div[2]/input')
password.click()
password.send_keys("Iononlaso0809")
checkbox = driver.find_element_by_name("cgv")
checkbox.click()
ad = driver.find_element_by_xpath('//*[@id="pageBody"]/div[4]/div/div[5]/button[1]')
ad.click()
driver.find_element_by_xpath('//*[@id="register"]/form/button').click()
time.sleep(4)
COLLEZIONE_BOTTONE = driver.find_element_by_xpath('//*[@id="menu-collection"]')
COLLEZIONE_BOTTONE.click()
time.sleep(2)
LA_MIA_COLLEZIONE_BOTTONE = driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[6]/div/a[1]')
LA_MIA_COLLEZIONE_BOTTONE.click()
time.sleep(3)
VENDITA_ESSIE_BOTTONE = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div/ul[3]/li[2]/div[2]/button[1]')
VENDITA_ESSIE_BOTTONE.click()
time.sleep(3)
driver.find_element_by_xpath("//input[@value='sellToKate']").click()
time.sleep(3)
WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
VENDITA_ESSIE_OKCONFIRM = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]')
VENDITA_ESSIE_OKCONFIRM.click()
Clintz += 2500
Punti_Esperienza += 50
time.sleep(3)
VENDITA_RANDY_BOTTONE = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div/ul[3]/li[5]/div[2]/button[1]')
VENDITA_RANDY_BOTTONE.click()
time.sleep(2)
VENDITA_RANDY_TOKATE = driver.find_element_by_xpath(".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
VENDITA_RANDY_TOKATE.click()
WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
VENDITA_RANDY_OKCONFIRM = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]')
VENDITA_RANDY_OKCONFIRM.click()
Clintz += 2500
Punti_Esperienza += 50
time.sleep(3)
NEGOZIO_BOTTONE = driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[10]/a')
NEGOZIO_BOTTONE.click()
time.sleep(3)
PACCHETTO_BOTTONE =  driver.find_element_by_xpath('//*[@id="pack_18"]')
PACCHETTO_BOTTONE.click()
time.sleep(4)
PARADOX_BOTTONE = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[18]')
PARADOX_BOTTONE.click()
SKEELZ_BOTTONE = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[27]')
SKEELZ_BOTTONE.click()
DOMINION_BOTTONE =  driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[4]')
DOMINION_BOTTONE.click()
KOMBOKA_BOTTONE = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[14]')
KOMBOKA_BOTTONE.click()
ACQUISTA_BOTTONE = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]')
ACQUISTA_BOTTONE.click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="menu-collection"]').click()
driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[6]/div/a[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/ html / body / div[3] / div[3] / form / ul[2] / li[1] / select / option[6]').click()
time.sleep(2)
driver.find_element_by_xpath('/ html / body / div[3] / div[3] / form / ul[2] / li[3] / select / option[3]').click()
time.sleep(2)
driver.find_element_by_xpath('/ html / body / div[3] / div[3] / form / ul[2] / li[3] / select / option[4]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[4]/select/option[2]').click()
time.sleep(2)
WebDriverWait(driver, 100).until(
    lambda driver: len(driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')) > 12)
elements = driver.find_elements_by_xpath('//button[@class="btn btn-add-deck js-toggle-deck"]')
for i in range(1, len(elements) + 1):
    elements[i-1].click()
    WebDriverWait(driver, 100).until(
        lambda driver: len(driver.find_elements_by_xpath('//button[@class="btn btn-add-deck js-toggle-deck"]')) == len(elements) - i)
driver.find_element_by_xpath('/ html / body / div[3] / div[3] / form / ul[2] / li[2] / select / option[2]').click()
time.sleep(5)

'''x = driver.find_elements_by_xpath('//small[@class="card-price"]')
for s in x:
    c = s.text.split(' ')
    Value = ""
    for n in range(len(c)):
        Value = Value + c[n]
    Value = int(Value)
    array.append(Value)'''
hihis = driver.find_elements_by_xpath('//button[@class="btn btn-remove-deck js-toggle-deck"]')
for g in range(len(hihis)):
    f = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    array2.append(f[g].text)
for i in range(1, len(hihis) - 7):
    hihis[i-1].click()
    WebDriverWait(driver, 100).until(
        lambda driver: len(driver.find_elements_by_xpath('//button[@class="btn btn-remove-deck js-toggle-deck"]')) == len(hihis) - i)
for m in range(25):
    lollo = len(driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]'))
    if lollo == 8:
        break
    else:
        gigi = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div/ul/li[1]/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", gigi)
        try:
            le = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 250 Clintz and 10 battle points')]")
        except:
            le = False
        try:
            lo = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
        except:
            lo = False
        try:
            la = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 9 000 Clintz and 100 battle points')]")
        except:
            la = False
        if lo or la or le:
            if lo:
                lo.click()
                Clintz += 2500
                Punti_Esperienza += 50
            elif la:
                la.click()
                Clintz += 9000
                Punti_Esperienza += 100
            else:
                le.click()
                Clintz += 250
                Punti_Esperienza += 10
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
        for i in range(10):
            try:
                WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_xpath('//span[@class="h6 card-name m-0"]').text == array2[m + 1])
                break
            except:
                print("Fiuu")
                time.sleep(1)

driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[1]/select/option[5]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[2]/select/option[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[3]/select/option[5]').click()
WebDriverWait(driver, 100).until(
            lambda driver: len(driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')) > 6)
'''
didis = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
op = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
for sg in range(0, len(didis)):
    array3.append(op[sg].text)
while o < 25:
    array4 = []
    kivni = False
    didism = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
    jijis = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
    omp = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(0, len(jijis)):
        array4.append(omp[i].text)
    if len(didism) == len(didis) - 1:
        count += 1
        didis.remove(didis[o-count])
        jijis[o-count].click()
        time.sleep(2)
        try:
            ile = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 250 Clintz and 10 battle points')]")
        except:
            ile = False
        try:
            ilo = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
        except:
            ilo = False
        try:
            ila = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 9 000 Clintz and 100 battle points')]")
        except:
            ila = False
        if ilo or ila or ile:
            if ilo:
                ilo.click()
                Clintz += 2500
                Punti_Esperienza += 50
            elif ila:
                ila.click()
                Clintz += 9000
                Punti_Esperienza += 100
            else:
                ile.click()
                Clintz += 250
                Punti_Esperienza += 10
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
            time.sleep(5)
            kivni = True
    if o >= len(set(array3) | set(array4)):
        break
    if kivni:
        array4 = []
        omp = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
        didism = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
        jijis = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
        for i in range(0, len(jijis)):
            array4.append(omp[i].text)
    didism[o - count].click()
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_xpath('//div[@class="bootbox-body"]'))
    gpl = driver.find_element_by_xpath('//div[@class="bootbox-body"]').text
    if gpl == 'Desideri cedere 500 XP a ' + array4[o - count] + ' per 1 000 Clintz?':
        lob = True
    else:
        lob = False
    if lob:
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]').click()
        Clintz -= 1000
        Punti_Esperienza += 20
    else:
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[1]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[1]').click()
    time.sleep(5)
    o += 1

arrayp = []
h = 0
count_0 = 0
didist = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
opp = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
for sga in range(0, len(didist)):
    arrayp.append(opp[sga].text)
while h < 25:
    array5 = []
    kivnim = False
    didismo = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
    jijiss = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
    omps = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(0, len(jijiss)):
        array5.append(omps[i].text)
    if len(didismo) == len(didist) - 1:
        count_0 += 1
        didist.remove(didist[h-count_0])
        jijiss[h-count_0].click()
        time.sleep(2)
        try:
            iles = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 250 Clintz and 10 battle points')]")
        except:
            iles = False
        try:
            ilos = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
        except:
            ilos = False
        try:
            ilas = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 9 000 Clintz and 100 battle points')]")
        except:
            ilas = False
        if ilos or ilas or iles:
            if ilos:
                ilos.click()
                Clintz += 2500
                Punti_Esperienza += 50
            elif ilas:
                ilas.click()
                Clintz += 9000
                Punti_Esperienza += 100
            else:
                iles.click()
                Clintz += 250
                Punti_Esperienza += 10
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
            time.sleep(5)
            kivnim = True
    if h >= len(set(arrayp) | set(array5)):
        break
    if kivnim:
        array5 = []
        omps = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
        didismo = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
        jijiss = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
        for i in range(0, len(jijiss)):
            array5.append(omps[i].text)
    didismo[h-count_0].click()
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_xpath('//div[@class="bootbox-body"]'))
    gpln = driver.find_element_by_xpath('//div[@class="bootbox-body"]').text
    if gpln == 'Desideri cedere 1 500 XP a ' + array5[h-count_0] + ' per 3 000 Clintz?':
        lobo = True
    else:
        lobo = False
    if lobo:
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]').click()
        Clintz -= 3000
        Punti_Esperienza += 30
    else:
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[1]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[1]').click()
    time.sleep(5)
    h += 1

livello = Esperienza()
Clintz += livello * 2000
print(Clintz)
arraypi = []
k = 0
count_00 = 0
didistt = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
oppp = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
for sga in range(0, len(didistt)):
    arraypi.append(oppp[sga].text)
while k < 25:
    array6 = []
    kivnimo = False
    didismos = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
    jijisss = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
    ompss = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(0, len(jijisss)):
        array6.append(ompss[i].text)
    if len(didismos) == len(didistt) - 1:
        count_00 += 1
        didistt.remove(didistt[k-count_00])
        jijisss[k-count_00].click()
        time.sleep(2)
        try:
            ileso = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 250 Clintz and 10 battle points')]")
        except:
            ileso = False
        try:
            iloso = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
        except:
            iloso = False
        try:
            ilaso = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 9 000 Clintz and 100 battle points')]")
        except:
            ilaso = False
        if iloso or ilaso or ileso:
            if iloso:
                iloso.click()
                Clintz += 2500
                Punti_Esperienza += 50
            elif ilaso:
                ilaso.click()
                Clintz += 9000
                Punti_Esperienza += 100
            else:
                ileso.click()
                Clintz += 250
                Punti_Esperienza += 10
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
            time.sleep(5)
            kivnimo = True
    if k >= len(set(arraypi) | set(array6)):
        break
    if kivnimo:
        array6 = []
        ompss = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
        didismos = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
        jijisss = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
        for i in range(0, len(jijisss)):
            array6.append(ompss[i].text)
    didismos[k-count_00].click()
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_xpath('//div[@class="bootbox-body"]'))
    gplno = driver.find_element_by_xpath('//div[@class="bootbox-body"]').text
    if gplno == 'Desideri cedere 3 000 XP a ' + array6[k-count_00] + ' per 6 000 Clintz?' and Clintz > 6000:
        loboc = True
    elif gplno == 'Desideri cedere 3 000 XP a ' + array6[k-count_00] + ' per 6 000 Clintz?' and not Clintz > 6000:
        break
    else:
        loboc = False
    if loboc:
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]').click()
        Clintz -= 6000
        Punti_Esperienza += 40
    else:
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[1]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[1]').click()
    time.sleep(5)
    k += 1


nonojik = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
jiji = True
contatore = 1
kio = 0
while jiji:
    if kio >= len(nonojik):
        break
    gigio = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div/ul/li[' + str(contatore) +']/div[2]/button[1]')
    driver.execute_script("arguments[0].click();", gigio)
    time.sleep(2)
    lipa = driver.find_element_by_xpath('//h4[@class="modal-title"]').text
    try:
        ale = driver.find_element_by_xpath(
            ".//*[contains(text(), ' Sell to Kate for 250 Clintz and 10 battle points')]")
    except:
        ale = False
    try:
        alo = driver.find_element_by_xpath(
            ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
    except:
        alo = False
    try:
        ala = driver.find_element_by_xpath(
            ".//*[contains(text(), ' Sell to Kate for 9 000 Clintz and 100 battle points')]")
    except:
        ala = False
    if alo or ala or ale and not (lipa == "Vendi Griffonmor sul Mercato" or lipa == "Vendi Enigma sul Mercato") :
        if alo:
            alo.click()
            Clintz += 2500
            Punti_Esperienza += 50
        elif ala:
            ala.click()
            Clintz += 9000         
            Punti_Esperienza += 100
        elif ale:
            ale.click()
            Clintz += 250
            Punti_Esperienza += 10
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
        time.sleep(5)
    elif lipa == "Vendi Griffonmor sul Mercato" or lipa == "Vendi Enigma sul Mercato":
        print("non posso venderla")
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
        contatore += 1
        time.sleep(3)
    kio += 1


driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[7]').click()
driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[7]/div/a[1]').click()
time.sleep(6)
kindk = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/form/ul[1]/li[3]/div/input')
kindk.click()
kindk.send_keys("Ashley")
driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/form/ul[1]/li[3]/div/span/button').click()
time.sleep(5)
minj = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[3]').text
print(minj)


'''
jijis = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
jijis[len(jijis) - 1].click()
WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]'))
driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
asinf = True
while asinf:
    print("Primo loop")
    array4 = []
    array5 = []
    array6 = []
    didism = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
    jijis = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
    omp = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(0, len(jijis)):
        array4.append(omp[i].text)
    elementini = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
    for r in range(len(elementini)):
        x = elementini[r].get_attribute('src')
        array5.append(x)
    try:
        for testo in array5:
            z = testo.split("_")[2].split("N")[1]
            array6.append(int(z))
    except:
        array5 = []
        array6 = []
        jijis = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
        jijis[len(jijis) - 1].click()
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
        elementini = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
        for r in range(len(elementini)):
            x = elementini[r].get_attribute('src')
            array5.append(x)
        for testo in array5:
            z = testo.split("_")[2].split("N")[1]
            array6.append(int(z))
    print(array6)
    countmo = 0
    pony = 0
    for i in range(len(array6)):
        if array6[i] == 1:
            countmo += 1
            pony = i
            break
    if countmo == 0:
        break
    card_self = array4[pony]
    didism[pony].click()
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]'))
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]').click()
    rimpiazzo = array5[pony].replace('_N1_', '_N2_')
    WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzo + '\"]'))
    Punti_Esperienza += 20
    Clintz -= 1000
    array4 = []
    array5 = []
    didism2 = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
    jijis2 = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
    omp2 = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(0, len(jijis2)):
        array4.append(omp2[i].text)
    elementini = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
    for r in range(len(elementini)):
        x = elementini[r].get_attribute('src')
        array5.append(x)
    p = array5.index(rimpiazzo)
    if len(didism2) < len(didism) or ((len(didism2) - len(didism)) != (len(jijis2) - len(jijis))):
        jijis2[p].click()
        try:
            ile = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 250 Clintz and 10 battle points')]")
        except:
            ile = False
        try:
            ilo = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
        except:
            ilo = False
        try:
            ila = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 9 000 Clintz and 100 battle points')]")
        except:
            ila = False
        if ilo or ila or ile:
            if ilo:
                ilo.click()
                Clintz += 2500
                Punti_Esperienza += 50
            elif ila:
                ila.click()
                Clintz += 9000
                Punti_Esperienza += 100
            else:
                ile.click()
                Clintz += 250
                Punti_Esperienza += 10
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
            WebDriverWait(driver, 100).until(lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzo + '\"]') == [])

asinfo = True
while asinfo:
    print("Secondo loop")
    liv1 = False
    array7 = []
    array8 = []
    array9 = []
    didismo = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
    jijiso = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
    ompo = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(0, len(jijiso)):
        array7.append(ompo[i].text)
    elementinis = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
    for r in range(len(elementinis)):
        xx = elementinis[r].get_attribute('src')
        array8.append(xx)
    print(array8)
    try:
        for testos in array8:
            zz = testos.split("_")[2].split("N")[1]
            array9.append(int(zz))
    except:
        array8 = []
        array9 = []
        jijiso = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
        jijiso[len(jijiso) - 1].click()
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
        elementinis = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
        for r in range(len(elementinis)):
            xx = elementinis[r].get_attribute('src')
            array8.append(xx)
        for testos in array8:
            zz = testos.split("_")[2].split("N")[1]
            array9.append(int(zz))
    print(array9)
    countmos = 0
    ponys = 0
    for i in range(len(array9)):
        if array9[i] == 2:
            countmos += 1
            ponys = i
            break
        elif array9[i] == 1:
            countmos += 1
            ponys = i
            liv1 = True
            break
    if countmos == 0:
        break
    card_selff = array7[ponys]
    didismo[ponys].click()
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]'))
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]').click()
    rimpiazzoo_liv1 = array8[ponys].replace('_N1_', '_N2_')
    rimpiazzoo = array8[ponys].replace('_N2_', '_N3_')
    if liv1:
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzoo_liv1 + '\"]'))
        Punti_Esperienza += 20
        Clintz -= 1000
    else:
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzoo + '\"]'))
        Punti_Esperienza += 30
        Clintz -= 3000
    array7 = []
    array8 = []
    didismo2 = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
    jijiso2 = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
    ompo2 = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(0, len(jijiso2)):
        array7.append(ompo2[i].text)
    elementinis = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
    for r in range(len(elementinis)):
        xx = elementinis[r].get_attribute('src')
        array8.append(xx)
    if liv1:
        pp = array8.index(rimpiazzoo_liv1)
    else:
        pp = array8.index(rimpiazzoo)
    if len(didismo2) < len(didismo) or ((len(didismo2) - len(didismo)) != (len(jijiso2) - len(jijiso))):
        jijiso2[pp].click()
        try:
            ilea = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 250 Clintz and 10 battle points')]")
        except:
            ilea = False
        try:
            iloa = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
        except:
            iloa = False
        try:
            ilaa = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 9 000 Clintz and 100 battle points')]")
        except:
            ilaa = False
        if iloa or ilaa or ilea:
            if iloa:
                iloa.click()
                Clintz += 2500
                Punti_Esperienza += 50
            elif ilaa:
                ilaa.click()
                Clintz += 9000
                Punti_Esperienza += 100
            else:
                ilea.click()
                Clintz += 250
                Punti_Esperienza += 10
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
            if liv1:
                WebDriverWait(driver, 100).until(lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzoo_liv1 + '\"]') == [])
            else:
                WebDriverWait(driver, 100).until(lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzoo + '\"]') == [])

livello = Esperienza()
Clintz += 2000*(livello - 1)

asinfos = True
while asinfos:
    print("Terzo loop")
    livello_inizio = Esperienza()
    liv1 = False
    liv2 = False
    array10 = []
    array11 = []
    array12 = []
    didismos = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
    jijisos = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
    ompos = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(0, len(jijisos)):
        array10.append(ompos[i].text)
    elementiniso = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
    for r in range(len(elementiniso)):
        xxx = elementiniso[r].get_attribute('src')
        array11.append(xxx)
    print(array11)
    try:
        for testoso in array11:
            zzz = testoso.split("_")[2].split("N")[1]
            array12.append(int(zzz))
    except:
        array11 = []
        array12 = []
        jijisos = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
        jijisos[len(jijisos) - 1].click()
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
        elementiniso = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
        for r in range(len(elementiniso)):
            xxx = elementiniso[r].get_attribute('src')
            array11.append(xxx)
        for testoso in array11:
            zzz = testoso.split("_")[2].split("N")[1]
            array12.append(int(zzz))
    print(array12)
    countmoso = 0
    ponyso = 0
    for i in range(len(array12)):
        if array12[i] == 3:
            countmoso += 1
            ponyso = i
            break
        elif array12[i] == 2:
            countmoso += 1
            ponyso = i
            liv2 = True
            break
        elif array12[i] == 1:
            countmoso += 1
            ponyso = i
            liv1 = True
            break
    if countmoso == 0:
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
    card_selfff = array10[ponyso]
    didismos[ponyso].click()
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]'))
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]').click()
    rimpiazzooo_liv1 = array11[ponyso].replace('_N1_', '_N2_')
    rimpiazzooo_liv2 = array11[ponyso].replace('_N2_', '_N3_')
    rimpiazzooo = array11[ponyso].replace('_N3_', '_N4_')
    if liv1:
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzooo_liv1 + '\"]'))
        Punti_Esperienza += 20
        Clintz -= 1000
    elif liv2:
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzooo_liv2 + '\"]'))
        Punti_Esperienza += 30
        Clintz -= 3000
    else:
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_xpath('//img[@src=\"' + rimpiazzooo + '\"]'))
        Punti_Esperienza += 40
        Clintz -= 6000
    livello_evoluzione = Esperienza()
    Clintz += 2000*(livello_evoluzione - livello_inizio)
    if Punti_Esperienza >= 1005:
        kosnikai = True
        Puoi_Vendere = True
        print("Io mi fermo qui!")
        break
    array10 = []
    array11 = []
    didismos2 = driver.find_elements_by_xpath('//button[@class="btn btn-xp-buy js-buy-xp"]')
    jijisos2 = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
    ompos2 = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(0, len(jijisos2)):
        array10.append(ompos2[i].text)
    elementiniso = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
    for r in range(len(elementiniso)):
        xxx = elementiniso[r].get_attribute('src')
        array11.append(xxx)
    if liv1:
        ppp = array11.index(rimpiazzooo_liv1)
    elif liv2:
        ppp = array11.index(rimpiazzooo_liv2)
    elif not (liv1 or liv2):
        ppp = array11.index(rimpiazzooo)
    if len(didismos2) < len(didismos) or ((len(didismos2) - len(didismos)) != (len(jijisos2) - len(jijisos))):
        jijisos2[ppp].click()
        try:
            ileas = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 250 Clintz and 10 battle points')]")
        except:
            ileas = False
        try:
            iloas = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
        except:
            iloas = False
        try:
            ilaas = driver.find_element_by_xpath(
                ".//*[contains(text(), ' Sell to Kate for 9 000 Clintz and 100 battle points')]")
        except:
            ilaas = False
        if iloas or ilaas or ileas:
            if iloas:
                iloas.click()
                Clintz += 2500
                Punti_Esperienza += 50
            elif ilaas:
                ilaas.click()
                Clintz += 9000
                Punti_Esperienza += 100
            else:
                ileas.click()
                Clintz += 250
                Punti_Esperienza += 10
            livello_vendita = Esperienza()
            Clintz += 2000*(livello_vendita - livello_evoluzione)
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
            if liv1:
                WebDriverWait(driver, 100).until(lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzooo_liv1 + '\"]') == [])
            elif liv2:
                WebDriverWait(driver, 100).until(lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzooo_liv2 + '\"]') == [])
            else:
                WebDriverWait(driver, 100).until(lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + rimpiazzooo + '\"]') == [])
    if Punti_Esperienza >= 1005:
        kosnikai = True
        Puoi_Vendere = True
        print("Io mi fermo qui!")
        break

if not kosnikai:
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[1]/select/option[6]').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[2]/select/option[2]').click()
    time.sleep(4)

asinfos = True
while asinfos and not kosnikai:
    livello_inizio = Esperienza()
    array13 = []
    array14 = []
    array15 = []
    jijisoso = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
    omposo = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(0, len(jijisoso)):
        array13.append(omposo[i].text)
    elementinisos = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
    for r in range(len(elementinisos)):
        xxxx = elementinisos[r].get_attribute('src')
        array14.append(xxxx)
    print(array14)
    try:
        for testosos in array14:
            zzzz = testosos.split("_")[1]
            array15.append(zzzz)
    except:
        array14 = []
        array15 = []
        jijisoso = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
        jijisoso[len(jijisoso) - 1].click()
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
        elementinisos = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
        for r in range(len(elementinisos)):
            xxxx = elementinisos[r].get_attribute('src')
            array14.append(xxxx)
        for testosos in array14:
            zzzz = testosos.split("_")[1]
            array15.append(zzzz)
    print(array15)
    countmosos = 0
    ponysos = 0
    for i in range(len(array15)):
        if array15[i] != "ENIGMA" and array15[i] != "GRIFFONMOR" and array15[i] != "KATE" and array15[i] != "VANSAAR":
            countmosos += 1
            ponysos = i
            break
    if countmosos == 0:
        break
    jijisoso[ponysos].click()
    try:
        ileaso = driver.find_element_by_xpath(
            ".//*[contains(text(), ' Sell to Kate for 250 Clintz and 10 battle points')]")
    except:
        ileaso = False
    try:
        iloaso = driver.find_element_by_xpath(
            ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
    except:
        iloaso = False
    try:
        ilaaso = driver.find_element_by_xpath(
            ".//*[contains(text(), ' Sell to Kate for 9 000 Clintz and 100 battle points')]")
    except:
        ilaaso = False
    if iloaso or ilaaso or ileaso:
        if iloaso:
            iloaso.click()
            Clintz += 2500
            Punti_Esperienza += 50
        elif ilaaso:
            ilaaso.click()
            Clintz += 9000
            Punti_Esperienza += 100
        else:
            ileaso.click()
            Clintz += 250
            Punti_Esperienza += 10
        livello_vendita = Esperienza()
        Clintz += 2000*(livello_vendita - livello_inizio)
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
        WebDriverWait(driver, 100).until(
                lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + array14[ponysos] + '\"]') == [])
    if Punti_Esperienza >= 1005:
        print("Io mi fermo")
        Puoi_Vendere = True
        time.sleep(3)
        break
print(Punti_Esperienza)
print(Clintz)
Nomsa = True

if Puoi_Vendere:
    driver.execute_script("window.open('http://www.yopmail.com/it/')")
    finestra_mail = driver.window_handles[1]
    finestra_urban = driver.window_handles[0]
    driver.switch_to.window(finestra_mail)
    gigi = driver.find_element_by_xpath('//*[@id="login"]')
    gigi.click()
    time.sleep(1)
    gigi.send_keys("nisadjasl" + str(c))
    driver.find_element_by_xpath('//*[@id="f"]/table/tbody/tr[1]/td[3]/input').click()
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_xpath('//*[@id="lrefr"]/span/span'))
    while Nomsa:
        driver.find_element_by_xpath('//*[@id="lrefr"]/span/span').click()
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_id('nbmail'))
        time.sleep(2)
        try:
            gigiasd = driver.find_element_by_id('nbmail').text.split(" ")[0]
            gigiasd = int(gigiasd)
            if gigiasd > 0:
                break
        except:
            pass
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_id('ifmail'))
    iframe = driver.find_element_by_id('ifmail')
    driver.switch_to.frame(iframe)
    driver.find_element_by_partial_link_text('https://www.urban-rivals.com/player/validation.php?').click()
    time.sleep(4)
    driver.switch_to.window(finestra_urban)
    time.sleep(2)

if Puoi_Vendere:
    print('Posso vendere')
    gommoso = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(len(gommoso)):
        if gommoso[i].text == "Enigma":
            Griffonmor = True
            print("Enigma dice il vero")
        elif gommoso[i].text == "Enigma":
            Griffonmor = True
            print("Enigma dice il vero")
        elif gommoso[i].text == "Kate":
            Kate = True
            print("Kate dice il vero")
        elif gommoso[i].text == "Griffonmor":
            Griffonmor = True
            print("Griffonmor dice il vero")

if Griffonmor:
    driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[7]').click()
    driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[7]/div/a[1]').click()
    time.sleep(4)
    asdasn = driver.find_element_by_name('search')
    asdasn.click()
    asdasn.send_keys('Enigma')
    asdasn.send_keys(Keys.RETURN)
    time.sleep(3)
    try:
        minj = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[3]').text
    except:
        minj = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[3]').text
    mentos = minj.split(" ")
    mentina = ""
    for i in range(len(mentos)):
        mentina = mentina + mentos[i]
    mentina = int(mentina)
    print(mentina)
    COLLEZIONE_BOTTONE = driver.find_element_by_xpath('//*[@id="menu-collection"]')
    COLLEZIONE_BOTTONE.click()
    time.sleep(2)
    LA_MIA_COLLEZIONE_BOTTONE = driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[6]/div/a[1]')
    LA_MIA_COLLEZIONE_BOTTONE.click()
    time.sleep(3)
    niasn = driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[6]/div/input')
    niasn.click()
    niasn.send_keys("Enigma")
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[6]/div/span/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div/ul/li/div[2]/button[1]').click()
    time.sleep(2)
    soldi = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/form/div[1]/input')
    soldi.click()
    soldi.send_keys(mentina - 100)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
    print("Finito")

if Griffonmor:
    driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[7]').click()
    driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[7]/div/a[1]').click()
    time.sleep(4)
    asdasno = driver.find_element_by_name('search')
    asdasno.click()
    asdasno.send_keys('Enigma')
    asdasno.send_keys(Keys.RETURN)
    time.sleep(3)
    try:
        minjo = driver.find_element_by_xpath(
            '/html/body/div[3]/div[5]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[3]').text
    except:
        minjo = driver.find_element_by_xpath(
            '/html/body/div[3]/div[4]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[3]').text
    mentoso = minjo.split(" ")
    mentinas = ""
    for i in range(len(mentoso)):
        mentinas = mentinas + mentoso[i]
    mentinas = int(mentinas)
    print(mentinas)
    COLLEZIONE_BOTTONE = driver.find_element_by_xpath('//*[@id="menu-collection"]')
    COLLEZIONE_BOTTONE.click()
    time.sleep(2)
    LA_MIA_COLLEZIONE_BOTTONE = driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[6]/div/a[1]')
    LA_MIA_COLLEZIONE_BOTTONE.click()
    time.sleep(3)
    niasno = driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[6]/div/input')
    niasno.click()
    niasno.send_keys("Enigma")
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[6]/div/span/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div/ul/li/div[2]/button[1]').click()
    time.sleep(2)
    soldis = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/form/div[1]/input')
    soldis.click()
    soldis.send_keys(mentinas - 100)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
    print("Finito")

if Kate:
    driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[7]').click()
    driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[7]/div/a[1]').click()
    time.sleep(4)
    asdasna = driver.find_element_by_name('search')
    asdasna.click()
    asdasna.send_keys('Kate')
    asdasna.send_keys(Keys.RETURN)
    time.sleep(3)
    try:
        minja = driver.find_element_by_xpath(
            '/html/body/div[3]/div[5]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[3]').text
    except:
        minja = driver.find_element_by_xpath(
            '/html/body/div[3]/div[4]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[3]').text
    mentosa = minja.split(" ")
    mentinaa = ""
    for i in range(len(mentosa)):
        mentinaa = mentinaa + mentosa[i]
    mentinaa = int(mentinaa)
    print(mentinaa)
    COLLEZIONE_BOTTONE = driver.find_element_by_xpath('//*[@id="menu-collection"]')
    COLLEZIONE_BOTTONE.click()
    time.sleep(2)
    LA_MIA_COLLEZIONE_BOTTONE = driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[6]/div/a[1]')
    LA_MIA_COLLEZIONE_BOTTONE.click()
    time.sleep(3)
    niasna = driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[6]/div/input')
    niasna.click()
    niasna.send_keys("Kate")
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[6]/div/span/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div/ul/li/div[2]/button[1]').click()
    time.sleep(2)
    soldia = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/form/div[1]/input')
    soldia.click()
    soldia.send_keys(mentinaa - 100)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
    print("Finito")

if Griffonmor:
    driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[7]').click()
    driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[7]/div/a[1]').click()
    time.sleep(4)
    asdasnm = driver.find_element_by_name('search')
    asdasnm.click()
    asdasnm.send_keys('Griffonmor')
    asdasnm.send_keys(Keys.RETURN)
    time.sleep(3)
    try:
        minjm = driver.find_element_by_xpath(
            '/html/body/div[3]/div[5]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[3]').text
    except:
        minjm = driver.find_element_by_xpath(
            '/html/body/div[3]/div[4]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[3]').text
    mentosm = minjm.split(" ")
    mentinam = ""
    for i in range(len(mentosm)):
        mentinam = mentinam + mentosm[i]
    mentinam = int(mentinam)
    print(mentinam)
    COLLEZIONE_BOTTONE = driver.find_element_by_xpath('//*[@id="menu-collection"]')
    COLLEZIONE_BOTTONE.click()
    time.sleep(2)
    LA_MIA_COLLEZIONE_BOTTONE = driver.find_element_by_xpath('//*[@id="navbar-menu"]/ul[1]/li[6]/div/a[1]')
    LA_MIA_COLLEZIONE_BOTTONE.click()
    time.sleep(3)
    niasnm = driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[6]/div/input')
    niasnm.click()
    niasnm.send_keys("Griffonmor")
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/ul[2]/li[6]/div/span/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div/ul/li/div[2]/button[1]').click()
    time.sleep(2)
    soldim = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/form/div[1]/input')
    soldim.click()
    soldim.send_keys(mentinam - 100)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
    print("Finito")







'''while Puoi_Vendere:
    array16 = []
    array17 = []
    array18 = []
    jijisosos = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
    omposos = driver.find_elements_by_xpath('//span[@class="h6 card-name m-0"]')
    for i in range(0, len(jijisosos)):
        array16.append(omposos[i].text)
    elementinisoso = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
    for r in range(len(elementinisoso)):
        xxxxx = elementinisoso[r].get_attribute('src')
        array17.append(xxxxx)
    print(array17)
    try:
        for testososo in array17:
            zzzzz = testososo.split("_")[1]
            array18.append(zzzzz)
    except:
        array17 = []
        array18 = []
        jijisosos = driver.find_elements_by_xpath('//button[@class="btn btn-sell-card js-sell"]')
        jijisosos[len(jijisosos) - 1].click()
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
        elementinisoso = driver.find_elements_by_xpath('//img[@class="card-picture js-lazyload"]')
        for r in range(len(elementinisoso)):
            xxxxx = elementinisoso[r].get_attribute('src')
            array17.append(xxxxx)
        for testososo in array17:
            zzzzz = testososo.split("_")[1]
            array18.append(zzzzz)
    print(array18)
    countmosos = 0
    ponysos = 0
    for i in range(len(array15)):
        if array15[i] == "ENIGMA" or array15[i] == "GRIFFONMOR" or array15[i] == "KATE" or array15[i] == "VANSAAR":
            countmosos += 1
            ponysos = i
            break
    if countmosos == 0:
        break
    jijisoso[ponysos].click()
    try:
        ileaso = driver.find_element_by_xpath(
            ".//*[contains(text(), ' Sell to Kate for 250 Clintz and 10 battle points')]")
    except:
        ileaso = False
    try:
        iloaso = driver.find_element_by_xpath(
            ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
    except:
        iloaso = False
    try:
        ilaaso = driver.find_element_by_xpath(
            ".//*[contains(text(), ' Sell to Kate for 9 000 Clintz and 100 battle points')]")
    except:
        ilaaso = False
    if iloaso or ilaaso or ileaso:
        if iloaso:
            iloaso.click()
            Clintz += 2500
            Punti_Esperienza += 50
        elif ilaaso:
            ilaaso.click()
            Clintz += 9000
            Punti_Esperienza += 100
        else:
            ileaso.click()
            Clintz += 250
            Punti_Esperienza += 10
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]'))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
        WebDriverWait(driver, 100).until(
                lambda driver: driver.find_elements_by_xpath('//img[@src=\"' + array14[ponysos] + '\"]') == [])
    if Punti_Esperienza >= 1005:
        print("Io mi fermo")
        break

