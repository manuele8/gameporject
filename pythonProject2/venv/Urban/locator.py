from selenium.webdriver.common.by import By
import values

class PaginaInizialeLocators(object):
    IDENTIFICATI_BOTTONE = (By.LINK_TEXT, "Identificati")
    IDENTIFICATI = (By.XPATH, '//a[@href="#login"]')
    EMAIL_CAMPO = (By.XPATH, '//*[@id="register"]/form/div[1]/input')
    LOGIN_EMAIL_CAMPO = (By.XPATH, '//*[@id="login"]/form/div[1]/input')
    PASSWORD_CAMPO = (By.XPATH, '//*[@id="register"]/form/div[2]/input')
    LOGIN_PASSWORD_CAMPO = (By.XPATH, '//*[@id="login"]/form/div[2]/input')
    CHECK_BOX = (By.NAME, "cgv")
    AD_OK_BOTTONE = (By.XPATH, '//*[@id="pageBody"]/div[4]/div/div[5]/button[1]')
    GIOCA_BOTTONE = (By.XPATH, '//*[@id="register"]/form/button')
    LOGIN_GIOCA_BOTTONE = (By.XPATH, '//*[@id="login"]/form/button')

class GiocaLocators(object):
    COLLEZIONE_BOTTONE = (By.XPATH, '//*[@id="menu-collection"]')
    LA_MIA_COLLEZIONE_BOTTONE = (By.XPATH, '//*[@id="navbar-menu"]/ul[1]/li[6]/div/a[1]')
    MASTERMIND_TESTO = (By.XPATH, '/html/body/div[3]/ul[4]/li[1]')

class CollezioneLocators(object):
    VENDITA_ESSIE_BOTTONE = (By.XPATH, '/html/body/div[3]/div[5]/div/div/ul[3]/li[2]/div[2]/button[1]')
    VENDITA_ESSIE_TOKATE = (By.XPATH, ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
    VENDITA_RANDY_BOTTONE = (By.XPATH, '/html/body/div[3]/div[5]/div/div/ul[3]/li[5]/div[2]/button[1]')
    VENDITA_RANDY_TOKATE = (By.XPATH, ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
    CONTROLLO_ = (By.XPATH, '/html/body/div[3]/div[5]/div/div/ul[3]/li[5]/div[1]/div[2]/span')
    NEGOZIO_BOTTONE = (By.XPATH, '//*[@id="navbar-menu"]/ul[1]/li[10]/a')
    ORDINE_RARITA_BOTTONE = (By.XPATH, '/ html / body / div[3] / div[3] / form / ul[2] / li[1] / select / option[6]')
    ORDINE_DECRESCENTE_BOTTONE = (By.XPATH, '/ html / body / div[3] / div[3] / form / ul[2] / li[2] / select / option[2]')
    ORDINE_CRESCENTE_BOTTONE = (By.XPATH, '/html/body/div[3]/div[3]/form/ul[2]/li[2]/select/option[1]')
    ORDINE_LIVELLO_MASSIMO_BOTTONE = (By.XPATH, '/html/body/div[3]/div[3]/form/ul[2]/li[1]/select/option[5]')
    ORDINE_SOLO_EVOLUZIONE_COMP_BOTTONE = (By.XPATH, '/html/body/div[3]/div[3]/form/ul[2]/li[3]/select/option[4]')
    ORDINE_FUORI_DAL_DECK_BOTTONE = (By.XPATH, '/html/body/div[3]/div[3]/form/ul[2]/li[3]/select/option[5]')
    FUORI_DAL_DECK_BOTTONE = (By.XPATH, '/ html / body / div[3] / div[3] / form / ul[2] / li[3] / select / option[4]')
    NUMERO_CARTE_BOTTONE_BLUFF = (By.XPATH, '/html/body/div[3]/div[3]/form/ul[2]/li[4]/select/option[3]')
    NUMERO_CARTE_BOTTONE = (By.XPATH, '/html/body/div[3]/div[3]/form/ul[2]/li[4]/select/option[2]')
    CHECK_NUMERO_CARTE = (By.XPATH, '//button[@class="btn btn-sell-card js-sell"]')
    AGGIUNGI_AL_DECK_BOTTONE = (By.XPATH, '//button[@class="btn btn-add-deck js-toggle-deck"]')
    AGGIUNGI_AL_DECK_BOTTONE2 = (By.XPATH, '/html/body/div[3]/div[5]/div/div/ul/li[1]/div[2]/button[3]')
    TOGLI_DAL_DECK_BOTTONE = (By.XPATH, '//button[@class="btn btn-remove-deck js-toggle-deck"]')
    NOMI_CARTE = (By.XPATH, '//span[@class="h6 card-name m-0"]')
    NOME_PRIMA_CARTA = (By.XPATH, '/html/body/div[3]/div[5]/div/div/ul/li[1]/div[1]/div[2]/span')
    VENDITA_BOTTONE = (By.XPATH, '//button[@class="btn btn-sell-card js-sell"]')
    PRIMO_BOTTONE_VENDITA = (By.XPATH, '/html/body/div[3]/div[5]/div/div/ul/li[1]/div[2]/button[1]')
    ALTRO_BOTTONE_VENDITA = (By.XPATH, '/html/body/div[3]/div[5]/div/div/ul/li/div[2]/button[1]')
    CAMPO_CLINTZ = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/input')
    COMUNE_BOTTONE = (By.XPATH, ".//*[contains(text(), ' Sell to Kate for 250 Clintz and 10 battle points')]")
    NON_COMUNE_BOTTONE = (By.XPATH, ".//*[contains(text(), ' Sell to Kate for 2 500 Clintz and 50 battle points')]")
    RARA_BOTTONE = (By.XPATH, ".//*[contains(text(), ' Sell to Kate for 9 000 Clintz and 100 battle points')]")
    VENDITA_BOTTONE_CONFERMA = (By.XPATH, "//button[@data-bb-handler='confirm']")
    CANCELLA_BOTTONE_CONFERMA = (By.XPATH, "//button[@data-bb-handler='cancel']")
    UPGRADE_BOTTONE = (By.XPATH, '//button[@class="btn btn-xp-buy js-buy-xp"]')
    UPGRADE_CONFERMA_BOTTONE = (By.XPATH, "//button[@data-bb-handler='confirm']")
    IMMAGINI_CARTE = (By.XPATH, '//img[@class="card-picture js-lazyload"]')
    RICERCA_BOTTONE = (By.XPATH, '/html/body/div[3]/div[3]/form/ul[2]/li[6]/div/input')


class NegozioLocators(object):
    PACCHETTO_BOTTONE = (By.XPATH, '//*[@id="pack_18"]')
    PARADOX_BOTTONE = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[18]')
    PARADOX_INPUT = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[18]/label/input')
    PUSSYCATS_BOTTONE = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[20]')
    PUSSYCATS_INPUT = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[20]/label/input')
    SKEELZ_BOTTONE = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[27]')
    SKEELZ_INPUT = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[27]/label/input')
    BERZERK_BOTTONE = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[3]')
    BERZERK_INPUT = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[3]/label/input')
    DOMINION_BOTTONE = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[4]')
    DOMINION_INPUT = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[4]/label/input')
    KOMBOKA_BOTTONE = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[14]')
    KOMBOKA_INPUT = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/div[1]/ul/li[14]/label/input')
    ACQUISTA_BOTTONE = (By.XPATH,'/html/body/div[5]/div/div/div[3]/button[2]')


class PacchettoLocators(object):
    FLIP_ALL_BOTTONE = (By.XPATH, '/html/body/div[3]/ul/li/button')
    CLINTZ_TESTO_COMPLETO = (By.XPATH, "/ html / body / div[3] / div[3] / div[2] / div[1] / p")
    CLINTZ_TESTO = (By.XPATH, "/html/body/div[3]/div[3]/div[2]/div[1]/p/span")
    BIOGRAFIA_BOTTONE = (By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div[1]/a')

class BiografiaLocators(object):
    DISCONNESSIONE_BOTTONE = (By.XPATH, '/html/body/div[3]/ul/li[3]')
    CONFERMA_DISCONNESSIONE_BOTTONE = (By.XPATH, '/html/body/div[10]/div/div/div[2]/button[2]')

class EmailLocators(object):
    MAIL_BUTTON = (By.XPATH, '//*[@id="login"]')
    INVIO_BOTTONE = (By.XPATH, '//*[@id="f"]/table/tbody/tr[1]/td[3]/input')
    AGGIORNAMENTO_MAIL_BOTTONE = (By.XPATH, '//*[@id="lrefr"]/span/span')
    NUMERO_MAIL = (By.ID, 'nbmail')
    IFRAME = (By.ID, 'ifmail')
    LINK_CONFERMA = (By.PARTIAL_LINK_TEXT, values.linktext)
    MESSAGGIO_SUCCESSO = (By.XPATH, '//div[@class="alert alert-success"]')

class MercatoLocators(object):
    MERCATO_BOTTONE = (By.XPATH, '//*[@id="navbar-menu"]/ul[1]/li[7]')
    IL_MERCATO_BOTTONE = (By.XPATH, '//*[@id="navbar-menu"]/ul[1]/li[7]/div/a[1]')
    RICERCA_BOTTONE = (By.NAME, 'search')
    VALORE_CARTA_1= (By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[3]')
    VALORE_CARTA_2 = (By.XPATH, '/html/body/div[3]/div[4]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[3]')
    NOME_CARTA = (By.XPATH, '//span[@class="h6 card-name text-character m-0"]')

class SearchResultsPageLocators(object):
    pass