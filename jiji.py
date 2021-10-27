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
array2 = ['🎶 Mi True Wireless Earbuds Air2 SE, Auricolare In-Ear ENC Smart Wireless Bluetooth 5.0\n\n‼️ Minimo Storico ‼️\n💰 A soli 14,99€ invece di 16,99€\n\n👉 https://amzn.to/3ieSW0y', '🖨 Stampante Multifunzione HP OfficeJet 8012e - 6 mesi di inchiostro inclusi con HP+\n\n‼️ Minimo Storico ‼️\n💰 A soli 99,99€ invece di 139,00€\n\n👉 https://amzn.to/3l2nHZV', '🍻 Peroni Cruda Birra - Cassa da 24 Bottiglie da 33cl, Non Pastorizzata - 7920 ml\n\n💰 A soli 20,20€ invece di 23,76€\n\n👉 https://amzn.to/3zmwI3K\n\nPerfetta per rinfrescarvi in estate 🔝', '🍻 Nastro Azzurro Birra Analcolica- Cassa da 24 x 33 cl (7.92 l)\n\n‼️ Minimo Storico ‼️\n💰 A soli 19,38€ invece di 23,92€\n\n👉 https://amzn.to/36Yst20', '💻 2021 Apple iPad Pro (12,9", Wi-Fi, 256GB) - Grigio siderale (5ª generazione)\n\n‼️ Minimo Storico ‼️\n💰 A soli 1.272,87€ invece di 1.329,00€\n\n👉 https://amzn.to/3i1sU2c\n\nMinimo per il SUPER iPad Pro con M1!', '📺 Samsung TV QE43Q64TAUXZT Serie Q60T Modello Q64T QLED Smart TV 43", con Alexa integrata, Ultra HD 4K, Wi-Fi, Silver, 2020, Esclusiva Amazon\n\n💰 A soli 339,21€ invece di 484,59€\n\n👉 https://amzn.to/3iMniYH\n\nSegnalata anche su @UsatoScontato, ottima occasione!\n\n✅ Sconto automatico visibile nel carrello in fase di pagamento 🛒', '❗️PREZZONE❗️\n🧦 Puma Sportsocken Cush Crew 6P Calzini Sportivi, Nero\n\n‼️ Minimo Storico ‼️\n💰 A soli 6,99€ invece di 15,99€\n\n👉 https://amzn.to/3ePVXUn\n\nPrezzone per ben 6 paia!', '🖥 Acer EG270Pbipx Monitor Gaming FreeSync Premium 27", Display IPS FHD\n\n‼️ Minimo Storico ‼️\n💰 A soli 176,55€ invece di 249,90€\n\n👉 https://amzn.to/3kPfqs7\n\nUn prezzo super accattivante per un 27”!', '❌ ERRORE o BOMBA? 💣\n👩 KYG Epilatore a Luce Pulsata Dispositivo IPL 500.000 Pulsazioni Utilizzo Bianco\n\n‼️ Minimo Storico ‼️\n💰 A soli 19,99€\n\n👉 https://amzn.to/3Bu4hTg', '📺 Samsung The Frame QLED 4K 2021 65LS03A Smart TV 65", Risoluzione 4K UHD\n\n‼️ Minimo Storico ‼️\n💰 A soli 1.618,99€ invece di 1.999,00€\n\n👉 https://amzn.to/2Tu2zQE\n\nUna tv MERAVIGLIOSA che arrederà il vostro salotto 😍\nPrezzo eccezionale per il 65”!', '😱 PREZZO DA URLO 😱\n💾 LaCie Mobile Drive, 2 TB, Hard Disk Esterno Portatile, USB-C, USB 3.0, Moon Silver, 2 anni di servizi Rescue (STHG2000400)\n\n💰 A soli 56,99€ invece di 134,99€\n\n👉 https://amzn.to/3BDa09m\n\n✅ Sconto automatico visibile nel carrello in fase di pagamento 🛒', '🔥 AFFARE 🔥\n🏡 Vivere UHSDO8-24 Amaca con Supporto Brasiliana, Cotone, 250 cm, Portata 200 kg Borsa da Trasporto inclu, Oasi Doppia, Oasis\n\n‼️ Minimo Storico ‼️\n💰 A soli 59,57€ invece di 158,95€\n\n👉 https://amzn.to/3zwo2rD\n\nTop per rilassarsi in queste calde giornate 😎', '👕 Lacoste Sport TH0123 T-Shirt, Marine, M Uomo\n\n💰 A soli 35,00€ invece di 45,00€\n\n👉 https://amzn.to/3zy0DWQ', '💻 HUAWEI MateBook X Pro 2021 Laptop, Display 3K FullView Touchscreen, Processore Intel i7-1165G7, 16 GB di memoria RAM, SSD da 1 TB, Intel Iris Xe Graphics, Win 10 Home, Layout Italiano, Space Gray\n\n‼️ Minimo Storico ‼️\n💰 A soli 1.489,66€ invece di 1.899,00€\n\n👉 https://amzn.to/3eRQtIG', '💣💣 BOMBA!!! 💣💣\n🎶 AUKEYPOWER Cuffie Bluetooth 5 in-ear, 28 ore di riproduzione con custodia di ricarica\n\n‼️ Minimo Storico ‼️\n💰 A soli 19,99€ invece di 39,99€\n✂️ Applica il coupon in pagina\n\n👉 https://amzn.to/3BB27kK', '🖨 Xiaomi Mi Portable Photo Printer, Stampante Laser Portatile, Carta fotografica lucida, Stampa termica, Connessione Bluetooth/USB/WLAN, Bianco, Versione Italiana\n\n💰 A soli 50,99€ invece di 69,99€\n\n👉 https://amzn.to/3x3ixPp', '📱 OnePlus 9 5G Smartphone Senza SIM con Fotocamera Hasselblad, 8 GB RAM + 128 GB, Blu (Arctic Sky)\n\n‼️ Minimo Storico ‼️\n💰 A soli 605,04€ invece di 719,00€\n\n👉 https://amzn.to/3eRVvW8', '💣💣 BOMBA!!! 💣💣\n🎒 Vans VN0A3I6R5S21 Unisex - Adulto , Marina, One Size\n\n‼️ Minimo Storico ‼️\n💰 A soli 18,95€ invece di 37,99€\n\n👉 https://amzn.to/3kN7Pu1']

for element in array2:
    if "BOMBA" in element.split('\n')[0] or "OFFERTA LAMPO" in element.split('\n')[0] or "PREZZONE" in element.split('\n')[0] or "ERRORE" in element.split('\n')[0] or "AFFARE" in element.split('\n')[0] or "PREZZO" in element.split('\n')[0]:
        print(element.split('\n')[1])
    else:
        print(element.split('\n')[0])
    if "💰 A soli" in element:
        elemento = (element.split("💰 A soli")[1].split('\n')[0])
        if elemento.count('€') == 1:
            print(elemento.split('€')[0])
        elif "invece di" in elemento:
            print(elemento.split('€')[0] + ' ' + elemento.split('invece di')[1].split('€')[0])
    elif "💰 A solo" in element:
        elemento = (element.split("💰 A solo")[1].split('\n')[0])
    if "https://" in element:
        elemento = element.split('https://')[1].split('\n')[0]
        print('https://' + elemento)