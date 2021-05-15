import pyperclip
import random
x = ""
question = input("Vuoi inserire tu un numero da indovinare? ")
if question == "s" or question == "S":
    ALL = input("Inserisci il numero da indovinare: ")
else:
    ALL = str(random.randrange(10000, 100000))
    print("Il numero da indovinare è: " + ALL)
array3 = []
for element in ALL:
    array3.append(element)
i = 1
gp = ""
while True:
    countq = 0
    countc = 0
    array5 = array3[:]
    gigi = input("Inserisci il tentativo numero " + str(i) + ': ')
    if gigi == "n" or gigi == "N":
        break
    while gigi == "r":
        if gigi == "r" or gigi == "R":
            gp = ""
            for lo in range(len(x) - 1):
                gp = gp + x[lo]
            print('Piccolo recap per chi fosse appena arrivato: ' + '\n' +'\n' + gp)
            pyperclip.copy('Piccolo recap per chi fosse appena arrivato: ' + '\n' +'\n' + gp)
            gigi = input("Inserisci il tentativo numero " + str(i) + ': ')
    for j in range(len(gigi)):
        if gigi[j] == ALL[j]:
            countq += 1
            array5.remove(gigi[j])
    for j in range(len(gigi)):
        if gigi[j] in array5 and gigi[j] != ALL[j]:
            countc += 1
            array5.remove(gigi[j])
    if countq == 5:
        print("Hai vinto, bravo")
    elif countq == 0 and countc > 1:
        print(str(countc) + ' cerchi per ' + str(gigi))
        x = x + str(countc) + ' cerchi per ' + str(gigi) + '\n'
        pyperclip.copy(str(countc) + ' cerchi per ' + str(gigi))
    elif countq == 0 and countc == 1:
        print(str(countc) + ' cerchio per ' + str(gigi))
        x = x + str(countc) + ' cerchio per ' + str(gigi) +'\n'
        pyperclip.copy(str(countc) + ' cerchio per ' + str(gigi))
    elif countq == 0 and countc == 0:
        print('Nulla per ' + str(gigi))
        x = x + 'Nulla per ' + str(gigi) + '\n'
        pyperclip.copy('Nulla per ' + str(gigi))
    elif countq == 1 and countc == 0:
        print(str(countq) + ' quadrato per ' + str(gigi))
        x = x + str(countq) + ' quadrato per ' + str(gigi) +'\n'
        pyperclip.copy(str(countq) + ' quadrato per ' + str(gigi))
    elif countq == 1 and countc == 1:
        print(str(countq) + ' quadrato e ' + str(countc) + ' cerchio per ' + str(gigi))
        x = x + str(countq) + ' quadrato e ' + str(countc) + ' cerchio per ' + str(gigi) +'\n'
        pyperclip.copy(str(countq) + ' quadrato e ' + str(countc) + ' cerchio per ' + str(gigi))
    elif countq == 1 and countc > 1:
        print(str(countq) + ' quadrato e ' + str(countc) + ' cerchi per ' + str(gigi))
        x = x + str(countq) + ' quadrato e ' + str(countc) + ' cerchi per ' + str(gigi) +'\n'
        pyperclip.copy(str(countq) + ' quadrato e ' + str(countc) + ' cerchi per ' + str(gigi))
    elif countq > 1 and countc == 0:
        print(str(countq) + ' quadrati per ' + str(gigi))
        x = x + str(countq) + ' quadrati per ' + str(gigi) +'\n'
        pyperclip.copy(str(countq) + ' quadrati per ' + str(gigi))
    elif countq > 1 and countc == 1:
        print(str(countq) + ' quadrati e ' + str(countc) + ' cerchio per ' + str(gigi))
        x = x + str(countq) + ' quadrati e ' + str(countc) + ' cerchio per ' + str(gigi) +'\n'
        pyperclip.copy(str(countq) + ' quadrati e ' + str(countc) + ' cerchio per ' + str(gigi))
    elif countq > 1 and countc > 1:
        print(str(countq) + ' quadrati e ' + str(countc) + ' cerchi per ' + str(gigi))
        x = x + str(countq) + ' quadrati e ' + str(countc) + ' cerchi per ' + str(gigi) +'\n'
        pyperclip.copy(str(countq) + ' quadrati e ' + str(countc) + ' cerchi per ' + str(gigi))
    i += 1
