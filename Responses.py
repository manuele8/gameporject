import random
from itertools import combinations_with_replacement
numero_finale = ""
array = [1, 2, 3, 4, 5, 6, 7]
arrayyy = []
initial_number = input("Inserisci un numero di 7 cifre con cui partire: ")
number_guess = input("Inserisci un numero di 7 cifre da 'indovinare': ")
for element in initial_number:
    arrayyy.append(int(element))
a, b, c, d, e, f, g = arrayyy[0], arrayyy[1], arrayyy[2], arrayyy[3], arrayyy[4], arrayyy[5], arrayyy[6]
def funzione(parametro):
    global a, b, c, d, e, f, g, numero_finale
    press_a = press_b = press_c = press_d = press_e = press_f = press_g = False
    if parametro == 1:
        press_a = True
    elif parametro == 2:
        press_b = True
    elif parametro == 3:
        press_c = True
    elif parametro == 4:
        press_d = True
    elif parametro == 5:
        press_e = True
    elif parametro == 6:
        press_f = True
    elif parametro == 7:
        press_g = True
    if press_a:
        a += 1
        b += 2
        c += 1
        d += -2
        e += +2
        f += 0
        g += -3
    elif press_b:
        a += -2
        b += 1
        c += -2
        d += -2
        e += +3
        f += -2
        g += -2
    elif press_c:
        a += 0
        b += -2
        c += 1
        d += 1
        e += +2
        f += -2
        g += -2
    elif press_d:
        a += 0
        b += 0
        c += 1
        d += 1
        e += -2
        f += 3
        g += -3
    elif press_e:
        a += -3
        b += 0
        c += -1
        d += 2
        e += 1
        f += -2
        g += 3
    elif press_f:
        a += 2
        b += 3
        c += 2
        d += -3
        e += 0
        f += 1
        g += 1
    elif press_g:
        a += -2
        b += -2
        c += -1
        d += -3
        e += 0
        f += 3
        g += 1
    if a > 9:
        a -= 10
    if a < 0:
        a += 10
    if b > 9:
        b -= 10
    if b < 0:
        b += 10
    if c > 9:
        c -= 10
    if c < 0:
        c += 10
    if d > 9:
        d -= 10
    if d < 0:
        d += 10
    if e > 9:
        e -= 10
    if e < 0:
        e += 10
    if f > 9:
        f -= 10
    if f < 0:
        f += 10
    if g > 9:
        g -= 10
    if g < 0:
        g += 10
    numero_finale = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)
    return numero_finale

x = [1, 2, 3, 4, 5, 6, 7]
do_not = False
arrayy = []
vocabolario = {'1': "premi_a", '2': "premi_b", '3': "premi_c", '4': "premi_d", '5': "premi_e", '6': "premi_f", '7': "premi_g"}
disp_rep = combinations_with_replacement('1234567', 20)
for element in disp_rep:
    if numero_finale == number_guess:
        break
    for elemento in element:
        funzione(int(elemento))
        arrayy.append(vocabolario[elemento])
        if numero_finale == number_guess:
            print("giusto")
            do_not = True
            break
    if do_not:
        print(arrayy)
        break
    else:
        a, b, c, d, e, f, g = arrayyy[0], arrayyy[1], arrayyy[2], arrayyy[3], arrayyy[4], arrayyy[5], arrayyy[6]
        arrayy = []

