import random

def choose_numbers(amount, total_amount):
    print(random.sample(range(0, total_amount + 1), amount))

choose_numbers(6, 49)

# za pomoca petli

lista = []

def choose_numbers2(amount, total):

    while len(lista) < amount:
        los = random.randint(0, total + 1)
        if los not in lista:
            lista.append(los)
        else:
            continue

choose_numbers2(6, 49)
print(lista)