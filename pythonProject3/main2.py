class Bambino:

    def __init__(self, peso, età, punteggio):
        self.peso = peso
        self.età = età
        self.punteggio = punteggio
        self.peso_cervello = età + punteggio**peso


    def morto_o_vivo(self):
        self.peso = self.peso + self.punteggio


bambino1 = Bambino(30, 15, 100)
print(bambino1.peso)
bambino1.morto_o_vivo()
print(bambino1.peso)




