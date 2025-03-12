#Q1

import sys
from random import *


class sorter:
    @staticmethod
    def randomList(k):
        x = []
        if k <= 0:
            return [9, 3, 4, 10, 100, -5, 2, 1, 4, 0, -12]
        else:
            for item in range(k):
                x.append(randint(10, 300))
            return x

    def __init__(self, debug=False):
        assert debug == False

    def sort(self, x):
        a = []
        indice = 0
        a.append(x[indice])
        if x[indice+1] > x[indice]:
            a.append(x[indice+1])
        else:
            a[indice] = x[indice+1]
            a.append(x[indice])

        for i in range(len(x) - len(a)):
            indice = self.binarySearsh(a, len(a), x[len(a)])
            if indice < len(a):
                if a[indice] > x[len(a)]:
                    a.insert(indice, x[len(a)])
                else:
                    a.insert(indice+1, x[len(a)])
            else:
                a.append(x[len(a)])
        return a

    def binarySearsh(self, arr, larr, x):
        first = 0
        last = larr
        pos = 0
        while first < last:
            meio = (first + last) // 2
            if arr[meio] == x:
                pos = meio
                first = last + 1
            else:
                if arr[meio] < x:
                    first = meio + 1
                else:
                    last = meio - 1
        if first == last:
            return first
        else:
            return pos


def main():
    s = sorter()
    lista1 = sorter.randomList(0)
    lista2 = s.sort(lista1)
    print("original list = %s" % lista1)
    print("sorted list = %s" % lista2)

    n = lista1[len(lista1)//2]
    b = s.binarySearsh(lista2, len(lista2), n)
    print("pos({}) -> sorted list[{}] and found = {}"
          .format(n, b, lista2[b]==n))

    n = 6
    b = s.binarySearsh(lista2, len(lista2), n)
    print("pos({}) -> sorted list[{}] and found = {}"
          .format(n, b, b < len(lista2) and lista2[b] == n))


if __name__ == '__main__':
    sys.exit(main())