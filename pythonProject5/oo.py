puzzle = [[2, 5, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 8, 4, 0, 0, 0, 7],
          [0, 0, 0, 1, 0, 0, 9, 0, 0],
          [0, 0, 6, 5, 0, 8, 0, 1, 9],
          [0, 7, 0, 0, 9, 0, 0, 4, 5],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [7, 0, 0, 6, 0, 0, 0, 8, 0],
          [6, 0, 0, 0, 0, 2, 7, 0, 0],
          [0, 3, 5, 4, 0, 0, 0, 0, 0]]

lista = {1, 2, 3, 4, 5, 6, 7, 8, 9}
righe = []
colonne = []
riga = []
colonna = []
boxes = []
box = []
x = []
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


def func():
    colums()
    rows()
    boxes_f()
    for i in range(len(puzzle)):
        for c in range(len(puzzle)):
            if puzzle[i][c] == 0:
                x.append(list(lista - set(colonne[c]) - set(puzzle[i]) - set(boxes[vocabolario[(i, c)]])))
    return x

func()
print(x)
for a in range(2):
    for i in range(len(puzzle)):
        for c in range(len(puzzle)):
            if puzzle[i][c] == 0:
                puzzle[i][c] = list(lista - set(colonne[c]) - set(puzzle[i]) - set(boxes[vocabolario[(i, c)]]))[a]

print(puzzle)

