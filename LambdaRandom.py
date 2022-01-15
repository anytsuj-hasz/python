import random
from functools import reduce

lista = [2, 5, 8, 10, 13, 17, 21, 23]

lista2 = random.choices(lista, k = 5)
print(lista2)
random.shuffle(lista2)
print(lista2)

def choose(amount, x):
    return random.sample(range(0, x), amount)

print(choose(3, 10))


lista = [2, 4, 7, 8, 10, 13, 15, 18]

newLista = list(filter(lambda x: x < 10, lista))
print(newLista)

newLista = list(map(lambda x:x*x, lista))
print(newLista)

print((lambda x: x * 2)(4))

suma = reduce(lambda x, y: x + y, lista)
print(suma)