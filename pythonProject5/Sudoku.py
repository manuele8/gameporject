puzzle = [[2, 5, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 8, 4, 0, 0, 0, 7],
          [0, 0, 0, 1, 0, 0, 9, 0, 0],
          [0, 0, 6, 5, 0, 8, 0, 1, 9],
          [0, 7, 0, 0, 9, 0, 0, 4, 5],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [7, 0, 0, 6, 0, 0, 0, 8, 0],
          [6, 0, 0, 0, 0, 2, 7, 0, 0],
          [0, 3, 5, 4, 0, 0, 0, 0, 0]]
righe = []
colonna = []
colonne = []
box = []
boxes = []
lista = {1, 2, 3, 4, 5, 6, 7, 8, 9}
vocabolario = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (1, 0): 0, (1, 1): 0, (1, 2): 0, (2, 0): 0, (2, 1): 0, (2, 2): 0,
               (0, 3): 1, (0, 4): 1, (0, 5): 1, (1, 3): 1, (1, 4): 1, (1, 5): 1, (2, 3): 1, (2, 4): 1, (2, 5): 1,
               (0, 6): 2, (0, 7): 2, (0, 8): 2, (1, 6): 2, (1, 7): 2, (1, 8): 2, (2, 6): 2, (2, 7): 2, (2, 8): 2,
               (3, 0): 3, (3, 1): 3, (3, 2): 3, (4, 0): 3, (4, 1): 3, (4, 2): 3, (5, 0): 3, (5, 1): 3, (5, 2): 3,
               (3, 3): 4, (3, 4): 4, (3, 5): 4, (4, 3): 4, (4, 4): 4, (4, 5): 4, (5, 3): 4, (5, 4): 4, (5, 5): 4,
               (3, 6): 5, (3, 7): 5, (3, 8): 5, (4, 6): 5, (4, 7): 5, (4, 8): 5, (5, 6): 5, (5, 7): 5, (5, 8): 5,
               (6, 0): 6, (6, 1): 6, (6, 2): 6, (7, 0): 6, (7, 1): 6, (7, 2): 6, (8, 0): 6, (8, 1): 6, (8, 2): 6,
               (6, 3): 7, (6, 4): 7, (6, 5): 7, (7, 3): 7, (7, 4): 7, (7, 5): 7, (8, 3): 7, (8, 4): 7, (8, 5): 7,
               (6, 6): 8, (6, 7): 8, (6, 8): 8, (7, 6): 8, (7, 7): 8, (7, 8): 8, (8, 6): 8, (8, 7): 8, (8, 8): 8,
               }

vocabolario_2 = {(0, 0): [0, 0], (0, 1): [0, 1], (0, 2): [0, 2], (0, 3): [1, 0], (0, 4): [1, 1], (0, 5): [1, 2], (0, 6): [2, 0], (0, 7): [2, 1], (0, 8): [2, 2],
                 (1, 0): [0, 3], (1, 1): [0, 4], (1, 2): [0, 5], (1, 3): [1, 3], (1, 4): [1, 4], (1, 5): [1, 5], (1, 6): [2, 3], (1, 7): [2, 4], (1, 8): [2, 5],
                 (2, 0): [0, 6], (2, 1): [0, 7], (2, 2): [0, 8], (2, 3): [1, 6], (2, 4): [1, 7], (2, 5): [1, 8], (2, 6): [2, 6], (2, 7): [2, 7], (2, 8): [2, 8],
                 (3, 0): [3, 0], (3, 1): [3, 1], (3, 2): [3, 2], (3, 3): [4, 0], (3, 4): [4, 1], (3, 5): [4, 2], (3, 6): [5, 0], (3, 7): [5, 1], (3, 8): [5, 2],
                 (4, 0): [3, 3], (4, 1): [3, 4], (4, 2): [3, 5], (4, 3): [4, 3], (4, 4): [4, 4], (4, 5): [4, 5], (4, 6): [5, 3], (4, 7): [5, 4], (4, 8): [5, 5],
                 (5, 0): [3, 6], (5, 1): [3, 7], (5, 2): [3, 8], (5, 3): [4, 6], (5, 4): [4, 7], (5, 5): [4, 8], (5, 6): [5, 6], (5, 7): [5, 7], (5, 8): [5, 8],
                 (6, 0): [6, 0], (6, 1): [6, 1], (6, 2): [6, 2], (6, 3): [7, 0], (6, 4): [7, 1], (6, 5): [7, 2], (6, 6): [8, 0], (6, 7): [8, 1], (6, 8): [8, 2],
                 (7, 0): [6, 3], (7, 1): [6, 4], (7, 2): [6, 5], (7, 3): [7, 3], (7, 4): [7, 4], (7, 5): [7, 5], (7, 6): [8, 3], (7, 7): [8, 4], (7, 8): [8, 5],
                 (8, 0): [6, 6], (8, 1): [6, 7], (8, 2): [6, 8], (8, 3): [7, 6], (8, 4): [7, 7], (8, 5): [7, 8], (8, 6): [8, 6], (8, 7): [8, 7], (8, 8): [8, 8]
                }
sudoku_completed = False
d_s = False


for i in range(len(puzzle)):
    if not(len(puzzle[i]) == len(puzzle) and len(puzzle) == 9):
        d_s = True
        break

if not d_s:
    def rows():
        for i in range(len(puzzle)):
            riga = puzzle[i]
            righe.append(riga)
        return righe


    def colums():
        global colonna
        for c in range(len(puzzle)):
            for i in range(len(puzzle)):
                colonna.append(puzzle[i][c])
            colonne.append(colonna)
            colonna = []
        return colonne


    def boxes_f():
        global box
        for c in range(0, 3):
            for i in range(0, 3):
                box.append(puzzle[c][i])
            if len(box) == 9:
                boxes.append(box)
                box = []
        for c in range(0, 3):
            for i in range(3, 6):
                box.append(puzzle[c][i])
                if len(box) == 9:
                    boxes.append(box)
                    box = []
        for c in range(0, 3):
            for i in range(6, 9):
                box.append(puzzle[c][i])
                if len(box) == 9:
                    boxes.append(box)
                    box = []
        for c in range(3, 6):
            for i in range(0, 3):
                box.append(puzzle[c][i])
                if len(box) == 9:
                    boxes.append(box)
                    box = []
        for c in range(3, 6):
            for i in range(3, 6):
                box.append(puzzle[c][i])
                if len(box) == 9:
                    boxes.append(box)
                    box = []
        for c in range(3, 6):
            for i in range(6, 9):
                box.append(puzzle[c][i])
                if len(box) == 9:
                    boxes.append(box)
                    box = []
        for c in range(6, 9):
            for i in range(0, 3):
                box.append(puzzle[c][i])
                if len(box) == 9:
                    boxes.append(box)
                    box = []
        for c in range(6, 9):
            for i in range(3, 6):
                box.append(puzzle[c][i])
                if len(box) == 9:
                    boxes.append(box)
                    box = []
        for c in range(6, 9):
            for i in range(6, 9):
                box.append(puzzle[c][i])
                if len(box) == 9:
                    boxes.append(box)
                    box = []
        return boxes


    '''def one_moment():
        boxes_f()
        rows()
        colums()
        count_1 = 0
        bacinella_0 = []
        for zx in range(len(puzzle)):
            milk = lista - set(colonne[zx])
            for post in milk:
                for gh in range(len(colonne[zx])):
                    if colonne[zx][gh] == 0 and post in (lista - set(righe[gh]) - set(boxes[vocabolario[(gh, zx)]])):
                        count_1 += 1
                        bacinella_0.append(gh)
                        bacinella_0.append(zx)
                if count_1 == 1:
                    puzzle[bacinella_0[0]][bacinella_0[1]] = post
                    count_1 = 0
                    bacinella_0.clear()
                    righe = []
                    colonne = []
                    boxes = []
                    rows()
                    colums()
                    boxes_f()
                else:
                    count_1 = 0
                    bacinella_0.clear()'''





    def controllo_sudoku():
        rows()
        colums()
        problems = False
        for i in range(len(puzzle)):
            if len(set(filter(lambda x: x != 0, righe[i]))) != len(list(filter(lambda x: x != 0, righe[i]))) or len(
                    set(filter(lambda x: x != 0, colonne[i]))) != len(list(filter(lambda x: x != 0, colonne[i]))):
                problems = True
                break
        for row in puzzle:
            for colum in row:
                if not (colum in lista or colum == 0):
                    problems = True
                    break
        if problems:
            return False
        else:
            return True

    def sudoku_finito():
        ciccio = False
        global sudoku_completed
        for c in range(len(puzzle)):
            for i in range(len(puzzle)):
                if puzzle[c][i] == 0:
                    ciccio = True
                    break
        if ciccio:
            sudoku_completed = False
        else:
            sudoku_completed = True
        return sudoku_completed


    def sudoku():
        global colonne
        global boxes
        global righe
        count = 0
        count_0 = 0
        count_1 = 0
        bacinella_0 = []
        bacinella = []
        array = []
        if controllo_sudoku():
            boxes_f()
            global sudoku_completed
            while not sudoku_completed:
                for zx in range(len(puzzle)):
                    milk = lista - set(colonne[zx])
                    for post in milk:
                        for gh in range(len(colonne[zx])):
                            if colonne[zx][gh] == 0 and post in (
                                    lista - set(righe[gh]) - set(boxes[vocabolario[(gh, zx)]])):
                                count_1 += 1
                                bacinella_0.append(gh)
                                bacinella_0.append(zx)
                        if count_1 == 1:
                            puzzle[bacinella_0[0]][bacinella_0[1]] = post
                            count_1 = 0
                            bacinella_0.clear()
                            righe = []
                            colonne = []
                            boxes = []
                            rows()
                            colums()
                            boxes_f()
                        else:
                            count_1 = 0
                            bacinella_0.clear()
                for n in range(len(puzzle)):
                    mil = lista - set(puzzle[n])
                    for pos in mil:
                        for v in range(len(puzzle[n])):
                            if puzzle[n][v] == 0 and pos in (lista - set(colonne[v]) - set(boxes[vocabolario[(n, v)]])):
                                count_0 += 1
                                bacinella.append(n)
                                bacinella.append(v)
                        if count_0 == 1:
                            puzzle[bacinella[0]][bacinella[1]] = pos
                            bacinella.clear()
                            count_0 = 0
                            righe = []
                            colonne = []
                            boxes = []
                            rows()
                            colums()
                            boxes_f()
                        else:
                            bacinella.clear()
                            count_0 = 0
                for m in range(len(boxes)):
                    x = lista - set(boxes[m])
                    for csa in x:
                        for k in range(len(boxes[m])):
                            if boxes[m][k] == 0 and csa in (lista - set(colonne[vocabolario_2[(m, k)][1]]) - set(
                                    righe[vocabolario_2[(m, k)][0]])):
                                count += 1
                                array.append((m, k))
                        if count == 1:
                            puzzle[vocabolario_2[array[0]][0]][vocabolario_2[array[0]][1]] = csa
                            array.clear()
                            count = 0
                            righe = []
                            colonne = []
                            boxes = []
                            rows()
                            colums()
                            boxes_f()
                        else:
                            array.clear()
                            count = 0
                for i in range(len(puzzle)):
                    for c in range(len(puzzle)):
                        if puzzle[i][c] == 0 and len(lista - set(colonne[c]) - set(puzzle[i]) - set(boxes[vocabolario[(i, c)]])) == 1:
                            puzzle[i][c] = list(lista - set(colonne[c]) - set(puzzle[i]) - set(boxes[vocabolario[(i, c)]]))[0]
                            colonne = []
                            boxes = []
                            righe = []
                            rows()
                            colums()
                            boxes_f()
                sudoku_finito()
                print(puzzle)
            return puzzle
        else:
            print("False")
    print(sudoku())
else:
    print("Il sudoku scritto non va bene!")





