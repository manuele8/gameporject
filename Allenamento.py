from itertools import combinations
def hand(hole_cards, community_cards):

    #definisci una scala generica

    def funzione(scala):
        scala.sort()
        for i in range(len(scala) - 1):
            if scala[i + 1] != scala[i] + 1:
                return False
        return True

    #definisci una lista con numeri uguali

    def controlla_se_uguali(lista):
        count = 0
        for i in range(len(lista) - 1):
            if lista[i + 1] == lista[i]:
                count += 1
        if count == len(lista) - 1:
            return True
        return False

    def controlla_se_uguali_v2(lista, n1, n2):
        listina = list(set(lista))
        if len(listina) == 2 and ((lista.count(listina[0]) == n1 and lista.count(listina[1]) == n2) or (
                lista.count(listina[0]) == n2 and lista.count(listina[1]) == n1)):
            return True
        return False


    #riconverti in termini di poker un array

    def riconverti(lista):
        vocabolario_reverse = {11: "J", 12: "Q", 13: "K", 14: "A"}
        for i in range(len(lista)):
            if lista[i] in vocabolario_reverse:
                lista[i] = vocabolario_reverse[lista[i]]
            else:
                lista[i] = str(lista[i])
        return lista

    #variabili

    simbols_vocab = {"♠": "p", "♦": "q", "♥": "c", "♣": "f"}
    letters_vocab = {"J": 11, "Q": 12, "K": 13, "A": 14}
    all_cards_list = []
    all_cards_list_mod = []
    lista_numeri = []
    listone = []
    lista_somme = []
    lista_elementi = []
    lista_momentanea = []
    lista_minore = []
    countp = 0
    countq = 0
    countc = 0
    countf = 0
    som = 0

    #crea tuple con tutte le carte (numeri, simboli)

    for hole_card in hole_cards:
        all_cards_list.append(hole_card)
    for community_card in community_cards:
        all_cards_list.append(community_card)
    for card in all_cards_list:
        if "10" not in card:
            if card[0] not in letters_vocab:
                all_cards_list_mod.append((int(card[0]), simbols_vocab[card[1]]))
            else:
                all_cards_list_mod.append((letters_vocab[card[0]], simbols_vocab[card[1]]))
        else:
            all_cards_list_mod.append((10, simbols_vocab[card[2]]))

    #controlla se si tratta di una carta alta

    def carta_alta():
        som = 0
        listone_carta_alta = []
        lista_elementi_carta_alta = []
        lista_somme_carta_alta = []
        lista_numeri_carta_alta = []
        for tupl in all_cards_list_mod:
            lista_numeri_carta_alta.append(tupl[0])
        all_possible_groups = list(combinations(lista_numeri_carta_alta, 5))
        for i in range(len(all_possible_groups)):
            all_possible_groups[i] = list(all_possible_groups[i])
        for element in all_possible_groups:
            for i in range(5):
                som = som + element[i]
            lista_somme_carta_alta.append(som)
            lista_elementi_carta_alta.append(element)
            som = 0
        arrayy = (lista_elementi_carta_alta[lista_somme_carta_alta.index(max(lista_somme_carta_alta))])
        arrayy.sort()
        array = riconverti(arrayy[::-1])
        return (("nothing", array))

    #controlla se si tratta di una coppia

    def coppia():
        som = 0
        contatore = 0
        listone_coppia = []
        lista_elementi_coppia = []
        lista_somme_coppia = []
        lista_numeri_coppia = []
        array = []
        for tupl in all_cards_list_mod:
            lista_numeri_coppia.append(tupl[0])
        all_possible_groups = list(combinations(lista_numeri_coppia, 2))
        for i in range(len(all_possible_groups)):
            all_possible_groups[i] = list(all_possible_groups[i])
        for element in all_possible_groups:
            '''if element == [2, 3, 4, 5, 14]:
                listone.append([1, 2, 3, 4, 5])'''
            if controlla_se_uguali(element):
                array = element
                break
        if array != []:
            for element in lista_numeri_coppia[:]:
                if element == array[0]:
                    lista_numeri_coppia.remove(element)
                    contatore += 1
                    if contatore == 2:
                        break
            array = list(set(array))
            array.append(max(lista_numeri_coppia))
            lista_numeri_coppia.remove(max(lista_numeri_coppia))
            array.append(max(lista_numeri_coppia))
            lista_numeri_coppia.remove(max(lista_numeri_coppia))
            array.append(max(lista_numeri_coppia))
            arra = riconverti(array)
            return (("pair", arra))
        else:
            return carta_alta()

    #controlla se si tratta di una doppia coppia

    def doppia_coppia():
        contatore = 0
        valore = 0
        som = 0
        listone_doppia_coppia = []
        lista_elementi_doppia_coppia = []
        lista_somme_doppia_coppia = []
        lista_numeri_doppia_coppia = []
        for tupl in all_cards_list_mod:
            lista_numeri_doppia_coppia.append(tupl[0])
        all_possible_groups = list(combinations(lista_numeri_doppia_coppia, 4))
        for i in range(len(all_possible_groups)):
            all_possible_groups[i] = list(all_possible_groups[i])
        for element in all_possible_groups:
            '''if element == [2, 3, 4, 5, 14]:
                listone.append([1, 2, 3, 4, 5])'''
            if controlla_se_uguali_v2(element, 2, 2):
                listone_doppia_coppia.append(element)
        if len(listone_doppia_coppia) > 1:
            for element in listone_doppia_coppia:
                for i in range(5):
                    som = som + element[i]
                lista_somme_doppia_coppia.append(som)
                lista_elementi_doppia_coppia.append(element)
                som = 0
            arrayy = (lista_elementi_doppia_coppia[lista_somme_doppia_coppia.index(max(lista_somme_doppia_coppia))])
            for element in arrayy:
                if max(arrayy) == element:
                    valore = element
            arrayy = list(set(arrayy))
            arrayy.remove(valore)
            array = []
            array.append(valore)
            array.append(arrayy[0])
            for element in lista_numeri_doppia_coppia[:]:
                if element == array[0]:
                    lista_numeri_doppia_coppia.remove(element)
                    contatore += 1
                    if contatore == 2:
                        break
            for element in lista_numeri_doppia_coppia[:]:
                if element == array[1]:
                    lista_numeri_doppia_coppia.remove(element)
                    contatore += 1
                    if contatore == 2:
                        break
            array.append(max(lista_numeri_doppia_coppia))
            array = riconverti(array)
            return (("two pair", array))
        elif len(listone_doppia_coppia) == 1:
            arrayy = listone_doppia_coppia[0]
            for element in arrayy:
                if max(arrayy) == element:
                    valore = element
            arrayy = list(set(arrayy))
            arrayy.remove(valore)
            array = []
            array.append(valore)
            array.append(arrayy[0])
            for element in lista_numeri_doppia_coppia[:]:
                if element == array[0]:
                    lista_numeri_doppia_coppia.remove(element)
                    contatore += 1
                    if contatore == 2:
                        break
            for element in lista_numeri_doppia_coppia[:]:
                if element == array[1]:
                    lista_numeri_doppia_coppia.remove(element)
                    contatore += 1
                    if contatore == 2:
                        break
            array.append(max(lista_numeri_doppia_coppia))
            array = riconverti(array)
            return (("two pair", array))
        else:
            return coppia()

    #controlla se si tratta di un tris

    def tris():
        som = 0
        contatore = 0
        listone_tris = []
        lista_elementi_tris = []
        lista_somme_tris = []
        lista_numeri_tris = []
        array = []
        for tupl in all_cards_list_mod:
            lista_numeri_tris.append(tupl[0])
        all_possible_groups = list(combinations(lista_numeri_tris, 3))
        for i in range(len(all_possible_groups)):
            all_possible_groups[i] = list(all_possible_groups[i])
        for element in all_possible_groups:
            '''if element == [2, 3, 4, 5, 14]:
                listone.append([1, 2, 3, 4, 5])'''
            if controlla_se_uguali(element):
                listone_tris.append(element)
        if len(listone_tris) > 1:
            for element in listone_tris:
                for i in range(3):
                    som = som + element[i]
                lista_somme_tris.append(som)
                lista_elementi_tris.append(element)
                som = 0
            array = (lista_elementi_tris[lista_somme_tris.index(max(lista_somme_tris))])
            for element in lista_numeri_tris[:]:
                if element == array[0]:
                    lista_numeri_tris.remove(element)
                    contatore += 1
                    if contatore == 3:
                        break
            array = list(set(array))
            array.append(max(lista_numeri_tris))
            lista_numeri_tris.remove(max(lista_numeri_tris))
            array.append(max(lista_numeri_tris))
            arra = riconverti(array)
            return (("three-of-a-kind", arra))
        elif len(listone_tris) == 1:
            array = listone_tris[0]
            for element in lista_numeri_tris[:]:
                if element == array[0]:
                    lista_numeri_tris.remove(element)
                    contatore += 1
                    if contatore == 3:
                        break
            array = list(set(array))
            array.append(max(lista_numeri_tris))
            lista_numeri_tris.remove(max(lista_numeri_tris))
            array.append(max(lista_numeri_tris))
            arra = riconverti(array)
            return (("three-of-a-kind", arra))
        else:
            return doppia_coppia()

    #controlla se si tratta di una scala normale

    def scala_normale():
        som = 0
        listone_scala = []
        lista_elementi_scala = []
        lista_somme_scala = []
        lista_numeri_scala = []
        for tupl in all_cards_list_mod:
            lista_numeri_scala.append(tupl[0])
        all_possible_groups = list(combinations(lista_numeri_scala, 5))
        for i in range(len(all_possible_groups)):
            all_possible_groups[i] = list(all_possible_groups[i])
        for element in all_possible_groups:
            element.sort()
            '''if element == [2, 3, 4, 5, 14]:
                listone.append([1, 2, 3, 4, 5])'''
            if funzione(element):
                listone_scala.append(element)
        if len(listone_scala) > 1:
            for element in listone_scala:
                for i in range(5):
                    som = som + element[i]
                lista_somme_scala.append(som)
                lista_elementi_scala.append(element)
                som = 0
            arrayy = (lista_elementi_scala[lista_somme_scala.index(max(lista_somme_scala))])
            array = riconverti(arrayy[::-1])
            return (("straight", array))
        elif len(listone_scala) == 1:
            arrayy = listone_scala[0]
            array = riconverti(arrayy[::-1])
            return (("straight", array))
        else:
            return tris()

    #controlla se si tratta di un colore

    def colore():
        som = countp = countq = countf = countc = 0
        lista_somme_colore = []
        lista_elementi_colore = []
        lista_colore = []
        lista_minore_colore = []
        for element in all_cards_list_mod:
            lista_colore.append(str(element[0]) + element[1])
        all_possible_groups2 = list(combinations(lista_colore, 5))
        for i in range(len(all_possible_groups2)):
            all_possible_groups2[i] = list(all_possible_groups2[i])
        for element in all_possible_groups2:
            for elemento in element:
                if 'p' in elemento:
                    countp += 1
                elif 'q' in elemento:
                    countq += 1
                elif 'c' in elemento:
                    countc += 1
                elif 'f' in elemento:
                    countf += 1
            if countp == 5 or countq == 5 or countc == 5 or countf == 5:
                lista_minore_colore.append(element)
            countp = 0
            countq = 0
            countc = 0
            countf = 0
        for element in lista_minore_colore:
            for i in range(len(element)):
                if len(element[i]) > 2:
                    element[i] = int(element[i][0] + element[i][1])
                else:
                    element[i] = int(element[i][0])
        #print(all_possible_groups2)
        for element in lista_minore_colore:
            element.sort()
        ''''if element == [2, 3, 4, 5, 14]:
                listone.append([1, 2, 3, 4, 5])'''
        if len(lista_minore_colore) > 1:
            for element in lista_minore_colore:
                for i in range(5):
                    som = som + element[i]
                lista_somme_colore.append(som)
                lista_elementi_colore.append(element)
                som = 0
            arrayy = (lista_elementi_colore[lista_somme_colore.index(max(lista_somme_colore))])
            array = riconverti(arrayy[::-1])
            return (("flush", array))
        elif len(lista_minore_colore) == 1:
            arrayy = lista_minore_colore[0]
            array = riconverti(arrayy[::-1])
            return (("flush", array))
        else:
            return scala_normale()

    #controlla se si tratta di un full

    def full():
        valore = 0
        som = 0
        listone_full = []
        lista_elementi_full = []
        lista_somme_full = []
        lista_numeri_full = []
        for tupl in all_cards_list_mod:
            lista_numeri_full.append(tupl[0])
        all_possible_groups = list(combinations(lista_numeri_full, 5))
        for i in range(len(all_possible_groups)):
            all_possible_groups[i] = list(all_possible_groups[i])
        for element in all_possible_groups:
            '''if element == [2, 3, 4, 5, 14]:
                listone.append([1, 2, 3, 4, 5])'''
            if controlla_se_uguali_v2(element, 2, 3):
                listone_full.append(element)
        if len(listone_full) > 1:
            for element in listone_full:
                for i in range(5):
                    som = som + element[i]
                lista_somme_full.append(som)
                lista_elementi_full.append(element)
                som = 0
            arrayy = (lista_elementi_full[lista_somme_full.index(max(lista_somme_full))])
            for element in arrayy:
                if arrayy.count(element) == 3:
                    valore = element
            arrayy = list(set(arrayy))
            arrayy.remove(valore)
            array = []
            array.append(valore)
            array.append(arrayy[0])
            array = riconverti(array)
            return (("full house", array))
        elif len(listone_full) == 1:
            arrayy = listone_full[0]
            for element in arrayy:
                if arrayy.count(element) == 3:
                    valore = element
            arrayy = list(set(arrayy))
            arrayy.remove(valore)
            array = []
            array.append(valore)
            array.append(arrayy[0])
            array = riconverti(array)
            return (("full house", array))
        else:
            return colore()

    #controlla se si tratta di un poker

    def poker():
        contatore = 0
        listone_poker = []
        lista_elementi_poker = []
        lista_somme_poker = []
        lista_numeri_poker = []
        array = []
        for tupl in all_cards_list_mod:
            lista_numeri_poker.append(tupl[0])
        all_possible_groups = list(combinations(lista_numeri_poker, 4))
        for i in range(len(all_possible_groups)):
            all_possible_groups[i] = list(all_possible_groups[i])
        for element in all_possible_groups:
            '''if element == [2, 3, 4, 5, 14]:
                listone.append([1, 2, 3, 4, 5])'''
            if controlla_se_uguali(element):
                array = element
                break
        if array != []:
            for element in lista_numeri_poker[:]:
                if element == array[0]:
                    lista_numeri_poker.remove(element)
                    contatore += 1
                    if contatore == 4:
                        break
            array = list(set(array))
            array.append(max(lista_numeri_poker))
            arra = riconverti(array)
            return (("four-of-a-kind", arra))
        else:
            return full()

    #controlla se si tratta di una scala colore

    def scala_colore():
        som = countp = countq = countf = countc = 0
        listone_scala_colore = []
        lista_somme_scala_colore = []
        lista_elementi_scala_colore = []
        lista_scala_colore = []
        lista_minore_scala_colore = []
        for element in all_cards_list_mod:
            lista_scala_colore.append(str(element[0]) + element[1])
        all_possible_groups2 = list(combinations(lista_scala_colore, 5))
        for i in range(len(all_possible_groups2)):
            all_possible_groups2[i] = list(all_possible_groups2[i])
        for element in all_possible_groups2:
            for elemento in element:
                if 'p' in elemento:
                    countp += 1
                elif 'q' in elemento:
                    countq += 1
                elif 'c' in elemento:
                    countc += 1
                elif 'f' in elemento:
                    countf += 1
            if countp == 5 or countq == 5 or countc == 5 or countf == 5:
                lista_minore_scala_colore.append(element)
            countp = 0
            countq = 0
            countc = 0
            countf = 0
        for element in lista_minore_scala_colore:
            for i in range(len(element)):
                if len(element[i]) > 2:
                    element[i] = int(element[i][0] + element[i][1])
                else:
                    element[i] = int(element[i][0])
        #print(all_possible_groups2)
        for element in lista_minore_scala_colore:
            element.sort()
            '''if element == [2, 3, 4, 5, 14]:
                listone.append([1, 2, 3, 4, 5])'''
            if funzione(element):
                listone_scala_colore.append(element)
        if len(listone_scala_colore) > 1:
            for element in listone_scala_colore:
                for i in range(5):
                    som = som + element[i]
                lista_somme_scala_colore.append(som)
                lista_elementi_scala_colore.append(element)
                som = 0
            arrayy = (lista_elementi_scala_colore[lista_somme_scala_colore.index(max(lista_somme_scala_colore))])
            array = riconverti(arrayy[::-1])
            return (("straight-flush", array))
        elif len(listone_scala_colore) == 1:
            arrayy = listone_scala_colore[0]
            array = riconverti(arrayy[::-1])
            return (("straight-flush", array))
        else:
            return poker()



    print(scala_colore())
    #scala_normale()

hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"])
