import ninja
f = open('gigi', 'r')
g = open('gigi', 'r')
e = open('gigi', 'r')
l = open('gigi', 'r')
k = open('gigi', 'r')
n = open("sto_file", "w")
o = open("sto_file_scegli_tu", "w")
m = open("percentuali_file", "w")
array = []
array2 = []
array0 = []
array4 = []
array5 = []
array6 = []
array7 = []
array8 = []
array9 = []
x = ""
count = 0
for i in range(len(g.readlines())):
    array0.append(e.readline().split(': ')[1].split(' + '))
    for element in f.readline().split(': ')[1].split(' + '):
        array.append(element.split('\n')[0])
f.close()
g.close()
for i in range(len(l.readlines())):
    array4.append(k.readline().split(':')[0])
for i in range(len(set(array))):
    array2.append(array.count(list(set(array))[i]))
for i in range(len(array2)):
    if array2[i] == max(array2):
        count += 1
        if count != array2.count(max(array2)):
            x = x + str(list(set(array))[i]) + " + "
        else:
            x = x + str(list(set(array))[i])
if array2.count(max(array2)) > 1:
    print("Ci sono " + str(array2.count(max(array2))) + " carte che compaiono " + str(max(array2)) + " volte: " + x)
elif array2.count(max(array2)) == 1:
    print("C'è una sola carta che compare " + str(max(array2)) + " volte: " + x)
array3 = x.split(' + ')
micocli = True
def scrivi_trova_carta(nome_carta):
    p = array.count(nome_carta)
    if p > 1:
        print("Ci sono " + str(p) + " " + nome_carta)
    elif p == 1:
        print("C'è una sola carta di " + nome_carta)
    for i in range(len(array0)):
        for j in range(len(array0[i])):
            if array0[i][j] == nome_carta or array0[i][j] == nome_carta + "\n":
                o.write(array4[i] + ": " + nome_carta + "\n")
g = input("Inserisci il nome di una carta: ")
if g in set(array):
    scrivi_trova_carta(g)
    print("Copie scritte")
else:
    print("Carta non trovata")
n.close()

for i in range(len(array2)):
    array6.append(str(array2[i]/len(array) * 100) + "%: " + list(set(array))[i])
array6.sort()
array6.reverse()
array7 = array2
array7.sort()
array7.reverse()
for i in range(len(array2)):
    array8.append(str(array2[i] / len(array0) * 100) + "%: " + list(set(array))[i])
array8.sort()
array8.reverse()
for i in range(len(array6)):
    array9.append(array6[i].split(': ')[1] + ": " + array8[i].split(': ')[0])
    m.write(array6[i].split(': ')[1] + ": " + str(array7[i]) + " (" + array6[i].split(': ')[0] + " per carte o " + array8[i].split(': ')[0] + " per profili)" + "\n")
print("Percentuali scritte")
m.close()
Enigma_Percentage = 0
PandemosCr_Percentage = 0
ElD10S_Percentage = 0
Kate_Percentage = 0
Griffonmor_Percentage = 0
Memento_Percentage = 0
Nadia_Percentage = 0
Death_Adder_Percentage = 0
Valore_Attuale_Enigma = 33
Valore_Attuale_PandemosCr = 200
Valore_Attuale_Kate = 95
Valore_Attuale_Griffonmor = 53
Valore_Attuale_ElD10S = 0
Valore_Attuale_Memento = 38
Valore_Attuale_Death_Adder = 15
Valore_Attuale_Nadia = 28
Valore_Attuale_Robert_Cobb = 30
Valore_Atteso = 0
for i in range(len(array9)):
    if array9[i].split(':')[0] == "Enigma":
        Enigma_Percentage = float(array9[i].split(': ')[1].split('%')[0])
    elif array9[i].split(':')[0] == "Pandemos Cr":
        PandemosCr_Percentage_Percentage = float(array9[i].split(': ')[1].split('%')[0])
    elif array9[i].split(':')[0] == "Griffonmor":
        Griffonmor_Percentage = float(array9[i].split(': ')[1].split('%')[0])
    elif array9[i].split(':')[0] == "El D10S":
        ElD10S_Percentage = float(array9[i].split(': ')[1].split('%')[0])
    elif array9[i].split(':')[0] == "Nadia":
        Nadia_Percentage = float(array9[i].split(': ')[1].split('%')[0])
    elif array9[i].split(':')[0] == "Death Adder":
        Death_Adder_Percentage = float(array9[i].split(': ')[1].split('%')[0])
    elif array9[i].split(':')[0] == "Robert Cobb":
        Robert_Cobb_Percentage = float(array9[i].split(': ')[1].split('%')[0])
    elif array9[i].split(':')[0] == "Memento":
        Memento_Percentage = float(array9[i].split(': ')[1].split('%')[0])
    elif array9[i].split(':')[0] == "Kate":
        Kate_Percentage = float(array9[i].split(': ')[1].split('%')[0])
x = input('Vuoi cercare su Internet (S/s o N/n): ')
if x == "S" or x == "s":
    Valore_Attuale_Enigma, Valore_Attuale_PandemosCr, Valore_Attuale_Griffonmor, Valore_Attuale_ElD10S, Valore_Attuale_Nadia, Valore_Attuale_Death_Adder, Valore_Attuale_Robert_Cobb, Valore_Attuale_Memento, Valore_Attuale_Kate = ninja.Faccio_Tutto_Io()
Valore_Atteso = (Valore_Attuale_Enigma * Enigma_Percentage + Valore_Attuale_PandemosCr*PandemosCr_Percentage + Valore_Attuale_Death_Adder*Death_Adder_Percentage + Valore_Attuale_Kate*Kate_Percentage + Valore_Attuale_Memento*Memento_Percentage + Valore_Attuale_Griffonmor*Griffonmor_Percentage + Valore_Attuale_Nadia*Nadia_Percentage + Valore_Attuale_Robert_Cobb*Robert_Cobb_Percentage) / 100
print("Il valore atteso per profilo risulta pari a: " + str(Valore_Atteso) + " milioni")


