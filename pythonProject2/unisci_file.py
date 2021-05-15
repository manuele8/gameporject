f = open("file1", "r")
e = open("file1", "r")
array = []
array2 = []
array3 = []
array4 = []
array5 = []
conto_Enigma = 0
conto_Griffonmor = 0
conto_Nadia = 0
conto_Death_Adder = 0
conto_Robert_Cobb = 0
conto_Memento = 0
conto_Kate = 0
x = 0
for i in range(len(f.readlines())):
    array.append(e.readline())
f.close()
e.close()
print(array)
g = open("file1", "w")
class Profili:
    def __init__(self, email, nome):
        self.email = email
        self.nome = nome

    def ritornanome(self):
        return self.nome

    def ritornaemail(self):
        return self.email


for i in range(len(array)):
    profilo = Profili(array[i].split(':')[0], array[i].split(': ')[1].split('\n')[0])
    array2.append(profilo)
for i in range(len(array2)):
    array3.append(array2[i].nome)
print(array3)
while len(array2) > 0:
    count = 0
    for i in range(len(array2)):
        if array2[i].nome == "Enigma":
            array4.append(array2[i])
            array2.remove(array2[i])
            count += 1
            break
    for i in range(len(array2)):
        if array2[i].nome == "Griffonmor":
            array4.append(array2[i])
            array2.remove(array2[i])
            count += 1
            break
    for i in range(len(array2)):
        if array2[i].nome == "Nadia":
            array4.append(array2[i])
            array2.remove(array2[i])
            count += 1
            break
    for i in range(len(array2)):
        if array2[i].nome == "Death Adder":
            array4.append(array2[i])
            array2.remove(array2[i])
            count += 1
            break
    for i in range(len(array2)):
        if array2[i].nome == "Robert Cobb":
            array4.append(array2[i])
            array2.remove(array2[i])
            count += 1
            break
    for i in range(len(array2)):
        if array2[i].nome == "Memento":
            array4.append(array2[i])
            array2.remove(array2[i])
            count += 1
            break
    for i in range(len(array2)):
        if array2[i].nome == "Kate":
            array4.append(array2[i])
            array2.remove(array2[i])
            count += 1
            break
    for i in range(len(array2)):
        if array2[i].nome != "Enigma" and array2[i].nome != "Griffonmor" and array2[i].nome != "Nadia" and array2[i].nome != "Death Adder" and array2[i].nome != "Robert Cobb" and array2[i].nome != "Memento" and array2[i].nome != "Kate":
            array5.append(array2[i])
            array2.remove(array2[i])
            count += 1
            break
    if count > 1:
        array4.append("\n")
for i in range(len(array4)):
    if array4[i] != "\n":
        g.write(array4[i].email + ": " + array4[i].nome + "\n")
    else:
        g.write(array4[i])
for i in range(len(array5)):
    g.write(array5[i].email + ": " + array5[i].nome + "\n")