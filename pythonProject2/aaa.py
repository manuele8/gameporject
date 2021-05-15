'''TxkRIRg50@yopmail.com: Enigma
rjzwWybcSQZXe19@yopmail.com: Nadia
rjzwWybcSQZXe43@yopmail.com: Enigma
rjzwWybcSQZXe49@yopmail.com: Griffonmor
rjzwWybcSQZXe56@yopmail.com: Enigma
rjzwWybcSQZXe58@yopmail.com: Kate + Death Adder
rjzwWybcSQZXe62@yopmail.com: Enigma + Enigma
rjzwWybcSQZXe86@yopmail.com: Nadia
rjzwWybcSQZXe134@yopmail.com: Enigma
rjzwWybcSQZXe136@yopmail.com: Enigma
XNGdalAJF4@yopmail.com: Nadia
XNGdalAJF8@yopmail.com: Nadia
XNGdalAJF11@yopmail.com: Nadia
XNGdalAJF31@yopmail.com: Enigma
XNGdalAJF39@yopmail.com: Enigma
XNGdalAJF44@yopmail.com: Kate
XNGdalAJF67@yopmail.com: Griffonmor
XNGdalAJF99@yopmail.com: Kate
aWkoYLlgExlSf5@yopmail.com: Griffonmor'''

array = []
array2 = []
sackn = 0
count_Enigma = 0
count_Griffonmor = 0
count_Nadia = 0
count_Death_Adder = 0
count_Kate = 0
count_Memento = 0
generical_count = 0
array_Enigma = []
array_Griffonmor = []
array_Nadia = []
array_Death_Adder = []
array_Kate = []
array_Memento = []
generical_array = []
generical_array_2 = []
def apri_sto_file():
    global array
    global array2
    fh = open("il_losg_cung_file", "r")
    g = open("il_losg_cung_file", "r")
    s = open("il_losg_cung_file", "r")
    for i in range(len(fh.readlines())):
        array.append(g.readline().split(": ")[1].split("\n")[0])
        array2.append(s.readline().split(":")[0])
    fh.close()
    g.close()
apri_sto_file()
print(array)
print(array2)
for element in array:
    if element == "Enigma":
        count_Enigma += 1
        array_Enigma.append(sackn)
    elif element == "Nadia":
        count_Nadia += 1
        array_Nadia.append(sackn)
    elif element == "Griffonmor":
        count_Griffonmor += 1
        array_Griffonmor.append(sackn)
    elif element == "Death Adder":
        count_Death_Adder += 1
        array_Death_Adder.append(sackn)
    elif element == "Memento":
        count_Memento += 1
        array_Memento.append(sackn)
    elif element == "Kate":
        count_Kate += 1
        array_Kate.append(sackn)
    else:
        generical_count += 1
        generical_array.append(sackn)
        generical_array_2.append(element)
    sackn += 1
print(array_Death_Adder)
print(array_Kate)
print(array_Nadia)
print(array_Griffonmor)
print(array_Memento)
print(array_Enigma)
print(generical_array)
print(generical_array_2)
print("Ci sono " + str(count_Death_Adder) + " Death Adder")
print("Ci sono " + str(count_Kate) + " Kate")
print("Ci sono " + str(count_Nadia) + " Nadia")
print("Ci sono " + str(count_Griffonmor) + " Griffonmor")
print("Ci sono " + str(count_Memento) + " Memento")
print("Ci sono " + str(count_Enigma) + " Enigma")
print("Ci sono " + str(generical_count) + " carte generiche")


if len(generical_array) > 0:
    for element in generical_array:
        print(array2[element] + ": " + generical_array_2[generical_array.index(element)])
if len(array_Enigma) > 0:
    for element in array_Enigma:
        print(array2[element] + ": " + "Enigma")
if len(array_Griffonmor) > 0:
    for element in array_Griffonmor:
        print(array2[element] + ": " + "Griffonmor")
if len(array_Nadia) > 0:
    for element in array_Nadia:
        print(array2[element] + ": " + "Nadia")
if len(array_Death_Adder) > 0:
    for element in array_Death_Adder:
        print(array2[element] + ": " + "Death Adder")
if len(array_Kate) > 0:
    for element in array_Kate:
        print(array2[element] + ": " + "Kate")
if len(array_Memento) > 0:
    for element in array_Memento:
        print(array2[element] + ": " + "Memento")






# Memento, Griffonmor, Death Adder, Kate, Nadia, Enigma