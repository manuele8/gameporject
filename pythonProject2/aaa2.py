import random
import numpy as np
contenitore = []
contenitore2 = []
array0 = []
array1 = []
array2 = []
count = 0
p = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\gigi', 'r')
e = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\gigi', 'r')
k = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\gigi', 'r')
km = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\gigi', 'r')
kma = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\gigiaskdn', 'w')
for i in range(len(p.readlines())):
    for element in e.readline().split(': ')[1].split(' + '):
        if element.split('\n')[0] == "Fraser":
            print('ciao')
        else:
            contenitore.append(element.split('\n')[0])
for i in range(len(k.readlines())):
    array0.append(km.readline().split(': ')[1].split(' + '))
p.close()
e.close()
k.close()
print(contenitore)
print(len(contenitore))
arr = np.array(contenitore)
print(len(arr))
arra = arr[arr != "Vansaar"]
arrab = arra[arra != "Timber"]
arrac = arrab[arrab != "Hugo"]
arrad = arrac[arrac != "Bridget"]
arrae = arrad[arrad != "Ashigaru"]
arraf = arrae[arrae != "Eyrik"]
arrag = arraf[arraf != "Ambre"]
arrah = arrag[arrag != "Eklore"]
arrai = arrah[arrah != "Morphun"]
arral = arrai[arrai != "Vholt"]
arram = arral[arral != "Solomon"]
arran = arram[arram != "Melody"]
arrap = arran[arran != "John Doom"]
arraq = arrap[arrap != "Mr Big Duke"]
arras = arraq[arraq != "Robert Cobb"]
arrat = arras[arras != "Memento"]
arraa = arrat[arrat != "Kate"]
for i in range(len(contenitore)):
    if contenitore[i] == "Vansaar" or contenitore[i] == "Timber" or contenitore[i] == "Hugo" or contenitore[i] == "Bridget" or contenitore[i] == "Ashigaru" or contenitore[i] == "Eyrik" or contenitore[i] == "Ambre" or contenitore[i] == "Eklore" or contenitore[i] == "Morphun" or contenitore[i] == "Vholt" or contenitore[i] == "Solomon" or contenitore[i] == "Melody" or contenitore[i] == "John Doom" or contenitore[i] == "Mr Big Duke" or contenitore[i] == "Robert Cobb" or contenitore[i] == "Memento" or contenitore[i] == "Kate":
        contenitore2.append(contenitore[i])
for i in range(len(contenitore2)):
    array1.append(8)
for i in range(len(array0) - len(contenitore2)):
    array1.append(7)
for i in range(10):
    g = ""
    x = random.choice(array1)
    if x == 7:
        for i in range(7):
            if i != x - 1:
                g = g + random.choice(arraa) + " + "
            else:
                g = g + random.choice(arraa)
        g = "gimmiloscoglionato" + str(count) + ": " + g
    else:
        for i in range(7):
            g = g + random.choice(arraa) + " + "
        g = "gimmiloscoglionato" + str(count) + ": " + g + random.choice(contenitore2)
    kma.write(g + '\n')
    count += 1
kma.close()


