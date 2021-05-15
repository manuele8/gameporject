f = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Segna_Valori.txt', 'r')
s = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Profiles_Sold_Wait.txt', 'r')
ss = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Profiles_Sold_Wait.txt', 'r')
d = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Profiles_Sold.txt', 'a')
dd = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Profiles_Sold.txt', 'r')
am = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Profiles_Sold_Wait.txt', 'r')
ams = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Profiles_Leveled_Up_2.txt', 'r')
amsd = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\gigiaskdn', 'r')

array = []
array0 = []
array3 = []
array4 = []
array5 = []
array6 = []
array8 = []
class ProfiliInVendita:
    def __init__(self,nome, valore):
        self.nome = nome
        self.valore = valore

    def ritornavalore(self):
        return self.valore

    def ritornanome(self):
        return self.nome

lines = f.readlines()
for line in lines:
    if line != "\n" and line != "":
        array0.append(line)
for element in array0:
    profilo = ProfiliInVendita(element.split(':')[0], element.split(': ')[1].split('\n')[0])
    array.append(profilo)
f.close()
l = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\gigiaskdn', 'r')
array1 = []
array2 = []
class Carte:
    def __init__(self, nome, valore):
        self.nome = nome
        self.valore = valore

    def ritornavalore(self):
        return self.valore

    def ritornanome(self):
        return self.nome

lines = l.readlines()
for line in lines:
    if line != "\n" and line != "":
        array1.append(line)
for element in array1:
    profilo = Carte(element.split(':')[0], element.split(': ')[1].split('\n')[0])
    array2.append(profilo)
for element in array:
    for elemento in array2:
        if element.nome in elemento.nome:
            if (float(elemento.valore) - float(element.valore)) > 0:
                array4.append(element.nome)
            break
linee = s.readlines()
for linea in linee:
    if linea != "\n" and linea != "":
        array5.append(linea)
x = len(dd.readlines())
for element in array4:
    for elemento in array5:
        if element in elemento.split(': ')[1].split('\n')[0]:
            if x == 0:
                d.write(elemento.split('\n')[0])
                x = 1
            else:
                d.write('\n' + elemento.split('\n')[0])
            ma = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Profiles_Sold_Wait.txt', 'r')
            liness = ma.readlines()
            mn = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Profiles_Sold_Wait.txt', 'w')
            for line in liness:
                if line.strip("\n") != elemento.split('\n')[0]:
                        mn.write(line)
            ma.close()
            mn.close()
v = am.readlines()
array7 = []
for element in v:
    if element != "" and element != '\n':
        array6.append(element.split(': ')[1].split('\n')[0])
for element in amsd:
    if element != "" and element != "\n":
        array7.append(element.split(':')[0].split('Valore Attuale ')[1])
for element in array7:
    if element not in array6:
        array8.append(element)
d = ams.readlines()
array9 = []
for element in array8:
    for elemento in d:
        if element in elemento:
            array9.append(elemento.split('\n')[0])
            break
print(array9)
