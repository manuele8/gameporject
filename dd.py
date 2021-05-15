import unisci
import multiprocessing
array = []
att = []
att2 = []
att3 = []
att4 = []
att7 = []
att8 = []
inputt = ""
inputto = ""
googgo = ""
lok = False

def accettazione(x):
    global inputt
    global inputto
    global att
    global att2
    att = []
    att2 = []
    count = 0
    count2 = 0
    arraio = []
    arraio2 = []
    for element in inputt:
        att.append(element)
    for elemento in x:
        att2.append(elemento)
    for i in range(len(att)):
        if att[i] != att2[i]:
            arraio.append(att[i])
        if att[i] == att2[i]:
            count += 1
            arraio2.append(i)
        if count > int(inputto):
            return False
        if i == len(att) - 1 and count < int(inputto):
            return False
        if i == len(att) - 1 and count == int(inputto):
            for elemen in sorted(arraio2, reverse=True):
                del att2[elemen]
            for elemeent in arraio:
                if elemeent not in att2:
                    count2 += 1
            if count2 == len(arraio):
                return True
            else:
                return False

def accettazione2(x):
    global inputt
    global googgo
    global att3
    global att4
    att3 = []
    att4 = []
    count = 0
    count2 = 0
    arraio = []
    arraio2 = []
    for element in inputt:
        att3.append(element)
    for elemento in x:
        att4.append(elemento)
    att5 = att3[:]
    for i in range(len(att3)):
        if att4[i] not in att5:
            arraio.append(att3[i])
        if att4[i] in att5 and att4[i] != att3[i]:
            count += 1
            arraio2.append(i)
            att5.remove(att4[i])
        if count > int(googgo) or att4[i] == att3[i]:
            return False
        if i == len(att3) - 1 and count < int(googgo):
            return False
        if i == len(att3) - 1 and count == int(googgo):
            for elemen in sorted(arraio2, reverse=True):
                del att4[elemen]
            for elemeent in att5:
                if elemeent not in att4:
                    count2 += 1
            if count2 == len(arraio):
                return True
            else:
                return False

def accettazione3(x):
    global inputt
    global inputto
    global att7
    global att8
    att7 = []
    att8 = []
    count = 0
    count2 = 0
    counti = 0
    countg = 0
    arraio = []
    arraio2 = []
    for element in inputt:
        att7.append(element)
    for elemento in x:
        att8.append(elemento)
    att10 = att7[:]
    for i in range(len(att7)):
        if att7[i] == att8[i]:
            counti += 1
            arraio2.append(i)
            att10.remove(att8[i])
    if counti > int(inputto):
        return False
    for i in range(len(att7)):
        if (att8[i] not in att10) and att8[i] != att7[i]:
            arraio.append(att7[i])
        if att8[i] in att10 and att8[i] != att7[i]:
            countg += 1
            arraio2.append(i)
            att10.remove(att8[i])
        if countg + counti > int(inputto) + int(googgo):
            return False
        if i == len(att7) - 1 and countg + counti < int(inputto) + int(googgo):
            return False
        if i == len(att7) - 1 and counti == int(inputto) and countg == int(googgo):
            for elemen in sorted(arraio2, reverse=True):
                del att8[elemen]
            for elemeent in att10:
                if elemeent not in att8:
                    count2 += 1
            if count2 == len(arraio):
                return True
            else:
                return False
def ricomincia(p):
    inputt = input("Inserisci un numero di 5 cifre: ")
    while inputt == "sugg" or inputt == "SUGG" or "info " in inputt or inputt == "n" or inputt == "N" or inputt == "r" or inputt == "R":
        if inputt == "sugg" or inputt == "SUGG":
            if len(array) < 10000 and p > 0:
                unisci.seow = 0
                unisci.array60 = []
                unisci.array60 = array[:]
                unisci.tutto()
            else:
                print("Mi spiace, ma non posso fornire suggerimenti ora, ci sono troppe combinazioni possibili!")
        elif "info " in inputt:
            elementasfm = inputt.split('info ')[1]
            unisci.xx = elementasfm
            unisci.array1 = array[:]
            unisci.potato()
        elif inputt == "n" or inputt == "N":
            break
        elif inputt == "r" or inputt == "R":
            lok = True
            break
        inputt = input("Inserisci un numero di 5 cifre: ")

def verifica():
    global array
    global inputt
    global inputto
    global googgo
    global lok
    p = 0
    jojjo = True
    lok = False
    while jojjo: #asido
        inputt = input("Inserisci un numero di 5 cifre: ")
        while inputt == "sugg" or inputt == "SUGG" or "info " in inputt or inputt == "n" or inputt == "N" or inputt == "r" or inputt == "R":
            if inputt == "sugg" or inputt == "SUGG":
                if len(array) < 10000 and p > 0:
                    unisci.seow = 0
                    unisci.array60 = []
                    unisci.array60 = array[:]
                    unisci.tutto()
                else:
                    print("Mi spiace, ma non posso fornire suggerimenti ora, ci sono troppe combinazioni possibili!")
            elif "info " in inputt:
                elementasfm = inputt.split('info ')[1]
                unisci.xx = elementasfm
                unisci.array1 = array[:]
                unisci.potato()
            elif inputt == "n" or inputt == "N":
                break
            elif inputt == "r" or inputt == "R":
                lok = True
                break
            inputt = input("Inserisci un numero di 5 cifre: ")
        if lok:
            break
        inputtos = input("Quanti quadrati/cerchi? ")
        inputto = inputtos.split(',')[0]
        while inputto == "n" or inputto == "N":
            if inputto == "n" or inputto == "N":
                ricomincia(p)
                inputtos = input("Quanti quadrati/cerchi? ")
                inputto = inputtos.split(',')[0]
        if ', ' not in inputtos:
            googgo = '0'
        else:
            googgo = inputtos.split(', ')[1]
        if googgo == "n" or googgo == "N":
            inputt = input("Inserisci un numero di 5 cifre: ")
            inputtos = input("Quanti quadrati/cerchi? ")
            inputto = inputtos.split(',')[0]
            if ', ' not in inputtos:
                googgo = '0'
            else:
                googgo = inputtos.split(', ')[1]
        if p == 0 and int(googgo) == 0:
            for i in range(100000):
                a = ""
                if len(str(i)) < 5:
                    for l in range(5 - len(str(i))):
                        a = a + '0'
                    a = a + str(i)
                    if accettazione(a):
                        array.append(a)
                if len(str(i)) == 5:
                    if accettazione(str(i)):
                        array.append(str(i))
            if len(array) >= 20:
                print("Ci sono più di 20 numeri in questa lista")
                print(array)
            else:
                for element in array:
                    print(element)
        elif p == 0 and int(inputto) == 0:
            for i in range(100000):
                a = ""
                if len(str(i)) < 5:
                    for l in range(5 - len(str(i))):
                        a = a + '0'
                    a = a + str(i)
                    if accettazione2(a):
                        array.append(a)
                if len(str(i)) == 5:
                    if accettazione2(str(i)):
                        array.append(str(i))
            if len(array) >= 20:
                print("Ci sono più di 20 numeri in questa lista")
                print(array)
            else:
                for element in array:
                    print(element)
        elif p > 0 and int(googgo) == 0:
            for element in array[:]:
                if not accettazione(str(element)):
                    array.remove(str(element))
            if len(array) >= 20:
                print("Ci sono più di 20 numeri in questa lista")
                print(array)
            else:
                for element in array:
                    print(element)
        elif p > 0 and int(inputto) == 0:
            for element in array[:]:
                if not accettazione2(str(element)):
                    array.remove(str(element))
            if len(array) >= 20:
                print("Ci sono più di 20 numeri in questa lista")
                print(array)
            else:
                for element in array:
                    print(element)
        elif p == 0 and int(inputto) > 0 and int(googgo) > 0:
            for i in range(100000):
                a = ""
                if len(str(i)) < 5:
                    for l in range(5 - len(str(i))):
                        a = a + '0'
                    a = a + str(i)
                    if accettazione3(a):
                        array.append(a)
                if len(str(i)) == 5:
                    if accettazione3(str(i)):
                        array.append(str(i))
            if len(array) >= 20:
                print("Ci sono più di 20 numeri in questa lista")
                print(array)
            else:
                for element in array:
                    print(element)
        elif p > 0 and int(inputto) > 0 and int(googgo) > 0:
            for element in array[:]:
                if not accettazione3(str(element)):
                    array.remove(str(element))
            if len(array) >= 20:
                print("Ci sono più di 20 numeri in questa lista")
                print(array)
            else:
                for element in array:
                    print(element)
        p += 1

verifica()
while lok:
    verifica()

#with multiprocessing.Pool(8) as pool:
    #pool.map(printamelo, array)