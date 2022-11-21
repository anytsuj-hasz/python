import random

lista = []

iloscElementow = int(input("Podaj ilość elementów w liście: "))

for i in range(0, iloscElementow):
    element = random.randint(0, 100)
    lista.append(element)

print(lista)
print(min(lista))
print(max(lista))

lista.sort()
print(lista)

newLista = list(map(lambda x: x**2, lista))
print(newLista)

newLista2 = list(filter(lambda x: x<50, lista))
print(newLista2)

print((lambda x: x * 4)(5))

# liczby podzielne przez 5 a nie przez 7
lista2 = []
for liczba in range(201):
    if (liczba % 5 == 0 and liczba % 7 != 0):
        lista2.append(liczba)

print(lista2)

# słownik

pokoje = {23: "Alek", 47: "Tomson", 89: "Ewa", 17: "Ania", 123: "Alek"}
nowy = {}
for key, name in pokoje.items():
    if name in nowy:
        nowy[name].append(key)
    else:
        nowy[name] = [key]

print(nowy)


