inputa = input('Vuoi visualizzare una lista generica di danni? ')
if inputa == "s" or inputa == "S":
    for n in range(6):
        for a in range(8):
            if a != 7:
                print('Danno = '+ str((1 + a)*(2**n)*3) + ' per (' + str(n) + ', ' + str(a) + ', ' + str(2*n + a + 5) + ')')
            else:
                print('Danno = ' + str((1 + a) * (2 ** n) * 3) + ' per (' + str(n) + ', ' + str(a) + ', ' + str(
                    2 * n + a + 6) + ')')
else:
    def visualizza(n, a):
        if a != 7:
            print('Danno = ' + str((1 + a) * (2 ** n) * 3) + ' per (' + str(n) + ', ' + str(a) + ', ' + str(
                2 * n + a + 5) + ')')
        else:
            print('Danno = ' + str((1 + a) * (2 ** n) * 3) + ' per (' + str(n) + ', ' + str(a) + ', ' + str(
                2 * n + a + 6) + ')')

    l = input('Indica il numero di raddoppia danni e di danni magici: ')
    while 1:
        if ', ' in l:
            x = int(l.split(',')[0])
            y = int(l.split(', ')[1])
            break
        else:
            print('Input non valido')
            input('Indica il numero di raddoppia danni e di danni magici: ')
    visualizza(x, y)





