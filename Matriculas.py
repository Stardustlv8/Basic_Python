import random

def alfabetico(a, b):
    a = (a % 8) + 1
    b = (b % 8) + 1
    a = str(a)
    b = str(b)
    cad = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G', '8':'H', '9':'I', '10':'J'}
    return cad[a] + cad[b]

def generatorMat(limit):
    valor = 11111111

    for i in range(limit):
        valor = valor + 1
        cad = str(valor)
        res = alfabetico(int(cad[2]), int(cad[3])) + cad
        print res, " ", random.randint(18, 95)

print generatorMat(100000)
