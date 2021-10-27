class Portiere:
    def __init__(self, voto, gol_subiti, ammonizione = 0, espulsione = 0, rigore_parato = 0, autogol = 0):
        self.voto = voto
        self.espulsione = espulsione
        self.autogol = autogol
        self.rigore_parato = rigore_parato
        self.gol_subiti = gol_subiti
        self.ammonizione = ammonizione

    def calcolo_voto_fanta(self):
        if self.gol_subiti >= 1:
            return (self.voto - self.gol_subiti - 0.5 * self.ammonizione - self.espulsione - 3 * self.autogol + 3 * self.rigore_parato)
        return (self.voto - 0.5 * self.ammonizione - self.espulsione - 3 * self.autogol + 3 * self.rigore_parato + 1)


lista_calciatori = ["Szczesny", "Acerbi", "De_Ligt", "Kjaer", "Manolas", "Calhanoglu", "Zielinski", "Candreva", "Muriel", "Berardi", "Morata"]

lista_calciatori[0] = Portiere(7, 1)
print(lista_calciatori[0].calcolo_voto_fanta())