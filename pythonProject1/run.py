o = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\il_mio_file_10.txt', 'r')
od = open(r'C:\Users\manue\PycharmProjects\pythonProject2\venv\Urban\il_mio_file_10.txt', 'r')
ks = len(od.readlines())
array = o.readlines()
'''if array[ks - 1].split('\n')[0] != array[ks - 1]:
    print('vero')'''
print(array)