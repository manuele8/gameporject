class VigenereCipher:
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.array_alphabet = []
        self.nuova_chiave = ""
        for letter in self.alphabet:
            self.array_alphabet.append(letter)

    def wrong_key(self):
        hod = False
        for letter in self.key:
            if letter not in self.alphabet:
                hod = True
                break
        if hod:
            return True
        return False

    def fun(self, a, b):
        if not self.wrong_key():
            if a in self.alphabet:
                x = self.array_alphabet.index(a)
                y = self.array_alphabet.index(b)
                return self.array_alphabet[(x + y) % len(self.alphabet)]
            return a

    def fun_cripted(self, a, b):
        if not self.wrong_key():
            if a in self.alphabet:
                x = self.array_alphabet.index(a)
                y = self.array_alphabet.index(b)
                return self.array_alphabet[(x - y) % len(self.alphabet)]
            return a

    def full_key(self, message):
        contenitore = []
        contenitore_2 = []
        for letter in self.key:
            contenitore.append(letter)
        for letter in message:
            contenitore_2.append(letter)
        contenitore_2 = list(filter(lambda n: n != " ", contenitore_2))
        i = 0
        count = 0
        for letter in message:
            if letter in self.alphabet and i < len(self.key):
                self.nuova_chiave = self.nuova_chiave + contenitore[i]
                i += 1
            elif letter not in self.alphabet:
                self.nuova_chiave = self.nuova_chiave + letter
            else:
                self.nuova_chiave = self.nuova_chiave + contenitore_2[count]
                count += 1
        return self.nuova_chiave

    def encode(self, message):
        if not self.wrong_key():
            self.full_key(message)
            cos = list(map(self.fun, message, self.nuova_chiave))
            codice = ""
            for i in range(len(cos)):
                codice = codice + cos[i]
            print(codice)
        else:
            print("Wrong key!")

    def decode(self, cripted_message):
        if not self.wrong_key():
            self.full_key(cripted_message)
            cos = list(map(self.fun_cripted, cripted_message, self.nuova_chiave))
            codice = ""
            for i in range(len(cos)):
                codice = codice + cos[i]
            print(codice)

        else:
            print("Wrong key!")


c = VigenereCipher("password", "abcdefghijklmnopqrstuvwxyz")
c.decode("CODEWARS")
