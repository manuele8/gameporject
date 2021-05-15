array = []


puzzle = [[3, 7, 0, 0, 1, 0, 0, 4, 0],
          [1, 0, 0, 0, 4, 0, 0, 0, 0],
          [0, 0, 0, 0, 7, 2, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 5, 7],
          [0, 0, 2, 9, 0, 0, 1, 0, 0],
          [0, 0, 4, 6, 0, 0, 8, 0, 0],
          [0, 4, 0, 0, 0, 0, 0, 0, 6],
          [0, 0, 8, 0, 0, 4, 9, 7, 1],
          [0, 0, 7, 0, 3, 0, 0, 0, 0]]


count = 0
rows()
colums()
boxes_f()
for m in range(len(boxes)):
    x = lista - set(boxes[m])
    for csa in x:
        for k in range(len(boxes[m])):
            if boxes[m][k] == 0 and csa in (
                    lista - set(colonne[vocabolario_2[(m, k)][1]]) - set(righe[vocabolario_2[(m, k)][0]])):
                count += 1
                array.append(m)
                array.append(k)
        if count == 1:
            boxes[array[0]][array[1]] = csa
            array.clear()
        else:
            array.clear()


            def one_moment():
                global righe
                global colonne
                global boxes
                boxes_f()
                rows()
                colums()
                count_1 = 0
                bacinella_0 = []
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
                            print(puzzle)
                            count_1 = 0
                            bacinella_0.clear()
                            righe = []
                            colonne = []
                            boxes = []
                            rows()
                            colums()
                            boxes_f()