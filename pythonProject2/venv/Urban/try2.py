f = open(r"C:\Users\manue\PycharmProjects\pythonProject2\Convertitore txt", "r")
e = open("try in txt", "r")
g = open("try 2 scrivi qui", "w")
array = []
array2 = []
array3 = []
array4 = []
x = 0
for i in range(len(f.readlines())):
    array.append(e.readline())
class Profili:
    def __init__(self, nome, valore, prezzo):
        self.nome = nome
        self.valore = valore
        self.prezzo = prezzo

    def ritornavalore(self):
        return self.valore

    def ritornaemail(self):
        return self.email

for i in range(len(array)):
    profilo = Profili(array[i].split(':')[0], array[i].split(': ')[1].split('\n')[0])
    array2.append(profilo)
for i in range(len(array2)):
    array3.append(int(array2[i].valore))
while len(array3) > 0:
    for i in range(len(array2)):
        if max(array3) == int(array2[i].valore):
            array4.append(array2[i])
            array3.remove(max(array3))
            break
for i in range(len(array4)):
    g.write(array4[i].email + ": " + array4[i].valore + '\n')
for i in range(len(array2)):
    x = x + int(array2[i].valore)
g.write('\n' + "TOTALE: " + str(x))