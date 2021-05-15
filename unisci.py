import pyperclip
import random
array60 = []
array9 = []
segnalatore = ""
imputt = ""
imputto = ""
giiggoo = ""
giiggo = ""
xx = ""
array290 = []
array1 = []
array2 = []
seow = 0
summ = 0
miccoli = []
def arrao():
    global miccoli
    for i in range(100000):
        if i < 10000:
            a = i
            for j in range(5 - len(str(i))):
                a = "0" + str(a)
            miccoli.append(a)
        else:
            miccoli.append(str(i))
    return miccoli
def tutto():
    global miccoli
    class Moment:
        def __init__(self, larr, elem):
            self.larr = larr
            self.elem = elem
    class Moment2:
        def __init__(self, larr2, elem2):
            self.larr2 = larr2
            self.elem2 = elem2
    global imputt
    global summ
    global seow
    global array290
    global imputto
    global array60
    global giiggoo
    global giiggo
    global array9
    array30 = []
    array9 = []
    att = []
    att2 = []
    att3 = []
    att4 = []
    att7 = []
    att8 = []
    imputt = ""
    imputto = ""
    giiggo = ""
    giiggoo = ""
    lokk = False

    def accettazionee(x):
        global imputt
        global imputto
        global att
        global att2
        att = []
        att2 = []
        counte = 0
        counte2 = 0
        arraioo = []
        arraioo2 = []
        for element in imputt:
            att.append(element)
        for elemento in x:
            att2.append(elemento)
        for i in range(len(att)):
            if att[i] != att2[i]:
                arraioo.append(att[i])
            if att[i] == att2[i]:
                counte += 1
                arraioo2.append(i)
            if counte > int(imputto):
                return False
            if i == len(att) - 1 and counte < int(imputto):
                return False
            if i == len(att) - 1 and counte == int(imputto):
                for elemen in sorted(arraioo2, reverse=True):
                    del att2[elemen]
                for elemeent in arraioo:
                    if elemeent not in att2:
                        counte2 += 1
                if counte2 == len(arraioo):
                    return True
                else:
                    return False

    def accettazionee2(x):
        global imputt
        global giiggo
        global att3
        global att4
        att3 = []
        att4 = []
        counte = 0
        counte2 = 0
        arraioo = []
        arraioo2 = []
        for element in imputt:
            att3.append(element)
        for elemento in x:
            att4.append(elemento)
        att5 = att3[:]
        for i in range(len(att3)):
            if att4[i] not in att5:
                arraioo.append(att3[i])
            if att4[i] in att5 and att4[i] != att3[i]:
                counte += 1
                arraioo2.append(i)
                att5.remove(att4[i])
            if counte > int(giiggo) or att4[i] == att3[i]:
                return False
            if i == len(att3) - 1 and counte < int(giiggo):
                return False
            if i == len(att3) - 1 and counte == int(giiggo):
                for elemen in sorted(arraioo2, reverse=True):
                    del att4[elemen]
                for elemeent in att5:
                    if elemeent not in att4:
                        counte2 += 1
                if counte2 == len(arraioo):
                    return True
                else:
                    return False

    def accettazionee3(x):
        global imputt
        global imputto
        global att7
        global att8
        att7 = []
        att8 = []
        counte = 0
        counte2 = 0
        countei = 0
        counteg = 0
        arraioo = []
        arraioo2 = []
        for element in imputt:
            att7.append(element)
        for elemento in x:
            att8.append(elemento)
        att10 = att7[:]
        for i in range(len(att7)):
            if att7[i] == att8[i]:
                countei += 1
                arraioo2.append(i)
                att10.remove(att8[i])
        if countei > int(imputto):
            return False
        for i in range(len(att7)):
            if (att8[i] not in att10) and att8[i] != att7[i]:
                arraioo.append(att7[i])
            if att8[i] in att10 and att8[i] != att7[i]:
                counteg += 1
                arraioo2.append(i)
                att10.remove(att8[i])
            if counteg + countei > int(imputto) + int(giiggo):
                return False
            if i == len(att7) - 1 and counteg + countei < int(imputto) + int(giiggo):
                return False
            if i == len(att7) - 1 and countei == int(imputto) and counteg == int(giiggo):
                for elemen in sorted(arraioo2, reverse=True):
                    del att8[elemen]
                for elemeent in att10:
                    if elemeent not in att8:
                        counte2 += 1
                if counte2 == len(arraioo):
                    return True
                else:
                    return False
    def valuta(my_try, guess):
        global imputto
        global summ
        global giiggo
        global imputt
        array30 = []
        counteqq, countecc = 0, 0
        array55 = array60[:]
        for element in guess:
            array30.append(element)
        for j in range(5):
            if my_try[j] == guess[j]:
                counteqq += 1
                array30.remove(my_try[j])
        for j in range(5):
            if my_try[j] in array30 and my_try[j] != guess[j]:
                countecc += 1
                array30.remove(my_try[j])
        imputto, giiggo, imputt = counteqq, countecc, my_try
        if countecc == 0:
            for element in array60[:]:
                if not accettazionee(element):
                    array55.remove(element)
        elif counteqq == 0:
            for element in array60[:]:
                if not accettazionee2(element):
                    array55.remove(element)
        elif counteqq > 0 and countecc > 0:
            for element in array60[:]:
                if not accettazionee3(element):
                    array55.remove(element)
        summ = summ + len(array55)
        return summ
    
    
    sums = []
    miccoli = []
    arrao()
    for elemento in miccoli:
        for element in array60[:]:
            valuta(elemento, element)
        class2 = Moment2(summ, elemento)
        sums.append(class2)
        summ = 0
    min_value = min((element.larr2 for element in sums))
    count_min_values = 0
    suggested_container = []
    suggested_numbers = ""
    for element in sums:
        if element.larr2 == min_value:
            count_min_values += 1
            suggested_container.append(element.elem2)
    if count_min_values == 1:
        print("Vi è un unico numero da suggerire: " + str(suggested_container[0]) + ' che comporta lunghezza media pari a:' + str(
            min_value / len(array60)))
    elif count_min_values < 10:
        for element in suggested_container:
            if suggested_numbers == "":
                suggested_numbers = element
            else:
                suggested_numbers = suggested_numbers + ', ' + element
        print(
            "Vi sono " + str(count_min_values) + " numeri da suggerire: " + suggested_numbers + ' che comportano lunghezza media pari a: ' + str(
                min_value / len(array60)))
    else:
        print("Vi sono " + str(count_min_values) + " numeri da suggerire e che comportano lunghezza media pari a: " + str(
            min_value / len(array60)))
        print("Suggerisco questi 3 numeri: " + str(random.choice(suggested_container)) + ', ' + str(
            random.choice(suggested_container)) + ', ' + str(random.choice(suggested_container)))




def potato():
    def accettazionee(x):
        global imputt
        global imputto
        global att
        global att2
        att = []
        att2 = []
        counte = 0
        counte2 = 0
        arraioo = []
        arraioo2 = []
        for element in imputt:
            att.append(element)
        for elemento in x:
            att2.append(elemento)
        for i in range(len(att)):
            if att[i] != att2[i]:
                arraioo.append(att[i])
            if att[i] == att2[i]:
                counte += 1
                arraioo2.append(i)
            if counte > int(imputto):
                return False
            if i == len(att) - 1 and counte < int(imputto):
                return False
            if i == len(att) - 1 and counte == int(imputto):
                for elemen in sorted(arraioo2, reverse=True):
                    del att2[elemen]
                for elemeent in arraioo:
                    if elemeent not in att2:
                        counte2 += 1
                if counte2 == len(arraioo):
                    return True
                else:
                    return False

    def accettazionee2(x):
        global imputt
        global giiggo
        global att3
        global att4
        att3 = []
        att4 = []
        counte = 0
        counte2 = 0
        arraioo = []
        arraioo2 = []
        for element in imputt:
            att3.append(element)
        for elemento in x:
            att4.append(elemento)
        att5 = att3[:]
        for i in range(len(att3)):
            if att4[i] not in att5:
                arraioo.append(att3[i])
            if att4[i] in att5 and att4[i] != att3[i]:
                counte += 1
                arraioo2.append(i)
                att5.remove(att4[i])
            if counte > int(giiggo) or att4[i] == att3[i]:
                return False
            if i == len(att3) - 1 and counte < int(giiggo):
                return False
            if i == len(att3) - 1 and counte == int(giiggo):
                for elemen in sorted(arraioo2, reverse=True):
                    del att4[elemen]
                for elemeent in att5:
                    if elemeent not in att4:
                        counte2 += 1
                if counte2 == len(arraioo):
                    return True
                else:
                    return False

    def accettazionee3(x):
        global imputt
        global imputto
        global att7
        global att8
        att7 = []
        att8 = []
        counte = 0
        counte2 = 0
        countei = 0
        counteg = 0
        arraioo = []
        arraioo2 = []
        for element in imputt:
            att7.append(element)
        for elemento in x:
            att8.append(elemento)
        att10 = att7[:]
        for i in range(len(att7)):
            if att7[i] == att8[i]:
                countei += 1
                arraioo2.append(i)
                att10.remove(att8[i])
        if countei > int(imputto):
            return False
        for i in range(len(att7)):
            if (att8[i] not in att10) and att8[i] != att7[i]:
                arraioo.append(att7[i])
            if att8[i] in att10 and att8[i] != att7[i]:
                counteg += 1
                arraioo2.append(i)
                att10.remove(att8[i])
            if counteg + countei > int(imputto) + int(giiggo):
                return False
            if i == len(att7) - 1 and counteg + countei < int(imputto) + int(giiggo):
                return False
            if i == len(att7) - 1 and countei == int(imputto) and counteg == int(giiggo):
                for elemen in sorted(arraioo2, reverse=True):
                    del att8[elemen]
                for elemeent in att10:
                    if elemeent not in att8:
                        counte2 += 1
                if counte2 == len(arraioo):
                    return True
                else:
                    return False
    global array1
    global array2
    global xx
    global giiggo
    global imputto
    global imputt
    x = ""
    for elemenlo in array1:
        array36 = array1[:]
        array2 = []
        ALL = ""
        ALL = elemenlo
        for element in ALL:
            array2.append(element)
        i = 1
        gp = ""
        countq = 0
        countc = 0
        array5 = array2[:]
        gigi = xx
        imputt = gigi
        if gigi == "n" or gigi == "N":
            break
        while gigi == "r":
            if gigi == "r" or gigi == "R":
                gp = ""
                for lo in range(len(x) - 1):
                    gp = gp + x[lo]
                print('Piccolo recap per chi fosse appena arrivato: ' + '\n' + '\n' + gp)
                pyperclip.copy('Piccolo recap per chi fosse appena arrivato: ' + '\n' + '\n' + gp)
                gigi = input("Inserisci il tentativo numero " + str(i) + ': ')
        for j in range(len(gigi)):
            if gigi[j] == ALL[j]:
                countq += 1
                array5.remove(gigi[j])
        for j in range(len(gigi)):
            if gigi[j] in array5 and gigi[j] != ALL[j]:
                countc += 1
                array5.remove(gigi[j])
        imputtosa = str(countq) + ', ' + str(countc)
        imputtoa = imputtosa.split(',')[0]
        giiggoa = imputtosa.split(', ')[1]
        imputto = imputtoa
        giiggo = giiggoa
        if int(giiggoa) == 0:
            for elementm in array1[:]:
                if not accettazionee(str(elementm)):
                    array36.remove(str(elementm))
        elif int(imputtoa) == 0:
            for elementm in array1[:]:
                if not accettazionee2(str(elementm)):
                    array36.remove(str(elementm))
        elif int(imputtoa) > 0 and int(giiggoa) > 0:
            for elementm in array1[:]:
                if not accettazionee3(str(elementm)):
                    array36.remove(str(elementm))
        if countq == 5:
            print(str(gigi) + ': ' + "Hai vinto, bravo, per " + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
        elif countq == 0 and countc > 1:
            print(str(gigi) + ': ' + str(countc) + ' cerchi per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
            x = x + str(gigi) + ': ' + str(countc) + ' cerchi per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )' + '\n'
            pyperclip.copy(str(gigi) + ': ' + str(countc) + ' cerchi per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
        elif countq == 0 and countc == 1:
            print(str(gigi) + ': ' + str(countc) + ' cerchio per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
            x = x + str(gigi) + ': ' + str(countc) + ' cerchio per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )' + '\n'
            pyperclip.copy(str(gigi) + ': ' + str(countc) + ' cerchio per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
        elif countq == 0 and countc == 0:
            print(str(gigi) + ': ' + 'Nulla per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
            x = x + str(gigi) + ': ' + 'Nulla per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )' + '\n'
            pyperclip.copy(str(gigi) + ': ' + 'Nulla per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
        elif countq == 1 and countc == 0:
            print(str(gigi) + ': ' + str(countq) + ' quadrato per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
            x = x + str(gigi) + ': ' + str(countq) + ' quadrato per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )' + '\n'
            pyperclip.copy(str(gigi) + ': ' + str(countq) + ' quadrato per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
        elif countq == 1 and countc == 1:
            print(str(gigi) + ': ' + str(countq) + ' quadrato e ' + str(countc) + ' cerchio per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
            x = x + str(gigi) + ': ' + str(countq) + ' quadrato e ' + str(countc) + ' cerchio per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )' + '\n'
            pyperclip.copy(str(gigi) + ': ' + str(countq) + ' quadrato e ' + str(countc) + ' cerchio per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
        elif countq == 1 and countc > 1:
            print(str(gigi) + ': ' + str(countq) + ' quadrato e ' + str(countc) + ' cerchi per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
            x = x + str(gigi) + ': ' + str(countq) + ' quadrato e ' + str(countc) + ' cerchi per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )' + '\n'
            pyperclip.copy(str(gigi) + ': ' + str(countq) + ' quadrato e ' + str(countc) + ' cerchi per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
        elif countq > 1 and countc == 0:
            print(str(gigi) + ': ' + str(countq) + ' quadrati per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
            x = x + str(gigi) + ': ' + str(countq) + ' quadrati per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )' + '\n'
            pyperclip.copy(str(gigi) + ': ' + str(countq) + ' quadrati per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
        elif countq > 1 and countc == 1:
            print(str(gigi) + ': ' + str(countq) + ' quadrati e ' + str(countc) + ' cerchio per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
            x = x + str(gigi) + ': ' + str(countq) + ' quadrati e ' + str(countc) + ' cerchio per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )' + '\n'
            pyperclip.copy(str(gigi) + ': ' + str(countq) + ' quadrati e ' + str(countc) + ' cerchio per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
        elif countq > 1 and countc > 1:
            print(str(gigi) + ': ' + str(countq) + ' quadrati e ' + str(countc) + ' cerchi per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
            x = x + str(gigi) + ': ' + str(countq) + ' quadrati e ' + str(countc) + ' cerchi per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )' + '\n'
            pyperclip.copy(str(gigi) + ': ' + str(countq) + ' quadrati e ' + str(countc) + ' cerchi per ' + str(ALL) + ' con lunghezza array pari a: ' + str(len(array36)) + ' ( ' + str(-len(array1) + len(array36)) + ' )')
