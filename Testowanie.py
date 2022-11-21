import random


def posortuj_liste(lista):
    liczbaElementow = len(lista)
    while liczbaElementow > 1:
        czyZamieniono = False
        for indexElementu in range(0, liczbaElementow-1):
            if lista[indexElementu] > lista[indexElementu+1]:
                lista[indexElementu], lista[indexElementu+1] = lista[indexElementu+1], lista[indexElementu]
                czyZamieniono = True
        liczbaElementow -= 1
        if not czyZamieniono:
            break

    return lista


lista =[]
i = 0

while i < 10:
    element = random.randint(0, 100)
    lista.append(element)
    i += 1

print(lista)
posortowanaLista = posortuj_liste(lista)
print(posortowanaLista)


# Sortowanie przez wstawianie
# def insertion_sort(lst):
#     for i in range(1, len(lst)):
#         j = i
#         while j > 0 and lst[j - 1] > lst[j]:
#             lst[j], lst[j - 1] = lst[j - 1], lst[j]
#             j -= 1
