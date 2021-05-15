class VigenereCipher:
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.array_alphabet = []
        self.repeated_key = key
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

    def encode(self, message):
        if not self.wrong_key():
            if len(message) > len(self.key):
                self.repeated_key = self.repeated_key * (int(len(message) / len(self.key)))
                for letter in self.repeated_key:
                    if len(message) > len(self.repeated_key):
                        self.repeated_key = self.repeated_key + letter
                    else:
                        break
            if len(message) <= len(self.repeated_key):
                cos = list(map(self.fun, message, self.repeated_key))
                codice = ""
                for i in range(len(cos)):
                    codice = codice + cos[i]
                print(codice)
        else:
            print("Wrong key!")

    def decode(self, cripted_message):
        if not self.wrong_key():
            if len(cripted_message) > len(self.key):
                self.repeated_key = self.repeated_key * (int(len(cripted_message) / len(self.key)))
                for letter in self.repeated_key:
                    if len(cripted_message) > len(self.repeated_key):
                        self.repeated_key = self.repeated_key + letter
                    else:
                        break
            if len(cripted_message) <= len(self.repeated_key):
                cos = list(map(self.fun_cripted, cripted_message, self.repeated_key))
                codice = ""
                for i in range(len(cos)):
                    codice = codice + cos[i]
                print(codice)
        else:
            print("Wrong key!")


c = VigenereCipher("password", "abcdefghijklmnopqrstuvwxyz")
stringa = "mangia"
for i in range(900):
    c.decode(stringa)
    stringa = c.encode(stringa)







