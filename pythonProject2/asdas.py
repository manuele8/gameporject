array = []
array0 = []
array1 = []
array2 = []
array3 = []
count = 0
x = 0
s = 0
f = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Valore Atteso', 'r')
e = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Valore Atteso', 'r')
h = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Valore Atteso', 'r')
l = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Valore Atteso', 'r')
p = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\il_mio_file', 'w')
m = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\il_mio_file', 'r')
r = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\il_mio_file', 'r')
class Profili:
    def __init__(self, email, valore):
        self.email = email
        self.valore = valore

    def ritornavalore(self):
        return self.valore

    def ritornaemail(self):
        return self.email

for i in range(len(f.readlines())):
    array0.append(e.readline())
for i in range(len(array0)):
    profilo = Profili(array0[i].split(':')[0], array0[i].split(': ')[1].split('\n')[0])
    array1.append(profilo)
for element in array1:
    array.append(int(element.valore))
while len(array) > 0:
    ninno = False
    for i in range(len(array)):
        if len(array) == 0:
            break
        x = x + array[i]
        array2.append(array1[i])
        array.pop(i)
        array1.pop(i)
        if x > 1055000000:
            osa = len(m.readlines())
            for element in array2:
                if array2.index(element) != len(array2) - 1:
                    if osa == 0:
                        p.write(element.email + ': ' + element.valore)
                        osa = 1
                    else:
                        p.write('\n' + element.email + ': ' + element.valore)
                else:
                    p.write('\n' + element.email + ': ' + element.valore + '\n' + '\n')
            array2 = []
            ninno = True
            break
        else:
            if len(array) == 0:
                break
            x = x + array[-(i+1)]
            array2.append(array1[-(i + 1)])
            array.pop(-(i+1))
            array1.pop(-(i + 1))
            if x > 1055000000:
                os = len(r.readlines())
                for element in array2:
                    if array2.index(element) != len(array2) - 1:
                        if os == 0:
                            p.write(element.email + ': ' + element.valore)
                            os = 1
                        else:
                            p.write('\n' + element.email + ': ' + element.valore)
                    else:
                        p.write('\n' + element.email + ': ' + element.valore + '\n' + '\n')
                array2 = []
                ninno = True
            break
    if ninno:
        count += 1
        x = 0

print(count)

f.close()
e.close()
h.close()
l.close()
p.close()
m.close()
r.close()

ansk = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\il_mio_file', 'r')
print(len(ansk.readlines()))
ka = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\il_mio_file', 'r')
hs = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\Valore Atteso', 'r')
hds = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\il_mio_file', 'a')
ad = ka.readlines()
bas = hs.readlines()
array11 = []
array22 = []
array33 = []
for element in ad:
    if element != "\n":
        array11.append(element.split('\n')[0])
print(len(array11))
for element in bas:
    if element != "\n":
        array22.append(element.split('\n')[0])
print(len(array22))
for i in range(len(array22)):
    if array22[i] not in array11:
        array33.append(array22[i])
print(len(array33))
hds.write('PROFILI NON UTILIZZATI: ' + '\n')
for element in array33:
    hds.write(element + '\n')