path = [(-50, 430), (55, 430), (104, 430), (147, 430), (192, 475), (245, 475), (281, 475), (317, 475), (349, 475),
             (380, 475), (417, 475), (452, 476), (500, 477), (540, 478), (576, 478), (613, 479), (647, 480), (666, 440),
             (678, 420), (679, 404), (673, 375), (663, 346), (652, 323), (631, 303), (600, 280), (569, 279), (542, 273),
             (498, 271), (468, 270), (430, 270), (397, 269), (381, 252), (350, 233), (345, 202), (345, 159), (357, 134),
             (369, 109), (395, 50), (426, 50), (462, 50), (496, 50), (540, 50), (576, 50), (623, 50), (664, 50),
             (702, 50), (750, 50), (790, 50), (830, 50), (868, 50), (900, 50), (943, 50), (978, 50), (1011, 50),
             (1043, 50)]

array = []
for element in path:
    array.append((element[0] - 60, element[1] - 50))

print(array)

stringa2 = 3
stringa3 = 5
stringa = f"/ {stringa2} \n pesce di aprile {stringa3} \n pesce di aprile parte 2"
print(stringa)