def prime_numbers_of_n(arraio):
    array = []
    g = (elementt for elementt in arraio)
    for elementt in g:
        for i in range(2, abs(elementt + 1)):
            if abs(elementt) % i == 0:
                array.append(i)
        print(array)
        for element in array[:]:
            for elemento in array[:]:
                if element % elemento == 0 and element != elemento:
                    array.remove(element)
                    break
    array = list(set(array))
    array.sort()
    array2 = []
    for elements in array:
        s = 0
        arra = []
        for elementi in arraio:
            if abs(elementi) % elements == 0:
                s += elementi
        arra.append(elements)
        arra.append(s)
        array2.append(arra)
    return array2

print(prime_numbers_of_n([15, 21, 24, 30, 45]))

def funzione(x):
    """
    :par: x
    return: True
    """
    return True

