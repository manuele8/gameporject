# -*- coding: utf-8 -*-
class Gionni:
    def __init__(self, x, y):
        self.x = x
        self.y = y

gionni = Gionni(1, 2)
gionni2 = Gionni(1, 2)

def equalsif(oggetto1, oggetto2):
    if oggetto1.x == oggetto2.x and oggetto1.y == oggetto2.y:
        return True
    return False

array = []
array2 = ['ð¶ Mi True Wireless Earbuds Air2 SE, Auricolare In-Ear ENC Smart Wireless Bluetooth 5.0\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 14,99â¬ invece di 16,99â¬\n\nð https://amzn.to/3ieSW0y', 'ð¨ Stampante Multifunzione HP OfficeJet 8012e - 6 mesi di inchiostro inclusi con HP+\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 99,99â¬ invece di 139,00â¬\n\nð https://amzn.to/3l2nHZV', 'ð» Peroni Cruda Birra - Cassa da 24 Bottiglie da 33cl, Non Pastorizzata - 7920 ml\n\nð° A soli 20,20â¬ invece di 23,76â¬\n\nð https://amzn.to/3zmwI3K\n\nPerfetta per rinfrescarvi in estate ð', 'ð» Nastro Azzurro Birra Analcolica- Cassa da 24 x 33 cl (7.92 l)\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 19,38â¬ invece di 23,92â¬\n\nð https://amzn.to/36Yst20', 'ð» 2021 Apple iPad Pro (12,9", Wi-Fi, 256GB) - Grigio siderale (5Âª generazione)\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 1.272,87â¬ invece di 1.329,00â¬\n\nð https://amzn.to/3i1sU2c\n\nMinimo per il SUPER iPad Pro con M1!', 'ðº Samsung TV QE43Q64TAUXZT Serie Q60T Modello Q64T QLED Smart TV 43", con Alexa integrata, Ultra HD 4K, Wi-Fi, Silver, 2020, Esclusiva Amazon\n\nð° A soli 339,21â¬ invece di 484,59â¬\n\nð https://amzn.to/3iMniYH\n\nSegnalata anche su @UsatoScontato, ottima occasione!\n\nâ Sconto automatico visibile nel carrello in fase di pagamento ð', 'âï¸PREZZONEâï¸\nð§¦ Puma Sportsocken Cush Crew 6P Calzini Sportivi, Nero\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 6,99â¬ invece di 15,99â¬\n\nð https://amzn.to/3ePVXUn\n\nPrezzone per ben 6 paia!', 'ð¥ Acer EG270Pbipx Monitor Gaming FreeSync Premium 27", Display IPS FHD\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 176,55â¬ invece di 249,90â¬\n\nð https://amzn.to/3kPfqs7\n\nUn prezzo super accattivante per un 27â!', 'â ERRORE o BOMBA? ð£\nð© KYG Epilatore a Luce Pulsata Dispositivo IPL 500.000 Pulsazioni Utilizzo Bianco\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 19,99â¬\n\nð https://amzn.to/3Bu4hTg', 'ðº Samsung The Frame QLED 4K 2021 65LS03A Smart TV 65", Risoluzione 4K UHD\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 1.618,99â¬ invece di 1.999,00â¬\n\nð https://amzn.to/2Tu2zQE\n\nUna tv MERAVIGLIOSA che arrederÃ  il vostro salotto ð\nPrezzo eccezionale per il 65â!', 'ð± PREZZO DA URLO ð±\nð¾ LaCie Mobile Drive, 2 TB, Hard Disk Esterno Portatile, USB-C, USB 3.0, Moon Silver, 2 anni di servizi Rescue (STHG2000400)\n\nð° A soli 56,99â¬ invece di 134,99â¬\n\nð https://amzn.to/3BDa09m\n\nâ Sconto automatico visibile nel carrello in fase di pagamento ð', 'ð¥ AFFARE ð¥\nð¡ Vivere UHSDO8-24 Amaca con Supporto Brasiliana, Cotone, 250 cm, Portata 200 kg Borsa da Trasporto inclu, Oasi Doppia, Oasis\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 59,57â¬ invece di 158,95â¬\n\nð https://amzn.to/3zwo2rD\n\nTop per rilassarsi in queste calde giornate ð', 'ð Lacoste Sport TH0123 T-Shirt, Marine, M Uomo\n\nð° A soli 35,00â¬ invece di 45,00â¬\n\nð https://amzn.to/3zy0DWQ', 'ð» HUAWEI MateBook X Pro 2021 Laptop, Display 3K FullView Touchscreen, Processore Intel i7-1165G7, 16 GB di memoria RAM, SSD da 1 TB, Intel Iris Xe Graphics, Win 10 Home, Layout Italiano, Space Gray\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 1.489,66â¬ invece di 1.899,00â¬\n\nð https://amzn.to/3eRQtIG', 'ð£ð£ BOMBA!!! ð£ð£\nð¶ AUKEYPOWER Cuffie Bluetooth 5 in-ear, 28 ore di riproduzione con custodia di ricarica\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 19,99â¬ invece di 39,99â¬\nâï¸ Applica il coupon in pagina\n\nð https://amzn.to/3BB27kK', 'ð¨ Xiaomi Mi Portable Photo Printer, Stampante Laser Portatile, Carta fotografica lucida, Stampa termica, Connessione Bluetooth/USB/WLAN, Bianco, Versione Italiana\n\nð° A soli 50,99â¬ invece di 69,99â¬\n\nð https://amzn.to/3x3ixPp', 'ð± OnePlus 9 5G Smartphone Senza SIM con Fotocamera Hasselblad, 8 GB RAM + 128 GB, Blu (Arctic Sky)\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 605,04â¬ invece di 719,00â¬\n\nð https://amzn.to/3eRVvW8', 'ð£ð£ BOMBA!!! ð£ð£\nð Vans VN0A3I6R5S21 Unisex - Adulto , Marina, One Size\n\nâ¼ï¸ Minimo Storico â¼ï¸\nð° A soli 18,95â¬ invece di 37,99â¬\n\nð https://amzn.to/3kN7Pu1']

for element in array2:
    if "BOMBA" in element.split('\n')[0] or "OFFERTA LAMPO" in element.split('\n')[0] or "PREZZONE" in element.split('\n')[0] or "ERRORE" in element.split('\n')[0] or "AFFARE" in element.split('\n')[0] or "PREZZO" in element.split('\n')[0]:
        print(element.split('\n')[1])
    else:
        print(element.split('\n')[0])
    if "ð° A soli" in element:
        elemento = (element.split("ð° A soli")[1].split('\n')[0])
        if elemento.count('â¬') == 1:
            print(elemento.split('â¬')[0])
        elif "invece di" in elemento:
            print(elemento.split('â¬')[0] + ' ' + elemento.split('invece di')[1].split('â¬')[0])
    elif "ð° A solo" in element:
        elemento = (element.split("ð° A solo")[1].split('\n')[0])
    if "https://" in element:
        elemento = element.split('https://')[1].split('\n')[0]
        print('https://' + elemento)