messaggio = "my secre"
chiave = "password"
alfabeto = "abcdefghijklmnopqrstuvwxyz"



contenitore = []
contenitore_2 = []


for letter in chiave:
    contenitore.append(letter)
for letter in messaggio:
    contenitore_2.append(letter)
contenitore_2 = list(filter(lambda n: n != " ", contenitore_2))


nuova_chiave = ""
i = 0
count = 0
for letter in messaggio:
    if letter in alfabeto and i < len(chiave):
        nuova_chiave = nuova_chiave + contenitore[i]
        i += 1
    elif letter not in alfabeto:
        nuova_chiave = nuova_chiave + letter
    else:
        nuova_chiave = nuova_chiave + contenitore_2[count]
        count += 1

print(nuova_chiave)

