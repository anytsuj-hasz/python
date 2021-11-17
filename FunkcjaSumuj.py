# Program liczący sumę liczb od 1 do podanej liczby
import time

def sumuj_do(liczba):
    suma = 0
    for liczba in range(1, liczba + 1):
        suma = suma + liczba
    return suma

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba + 1)])     # wyrażenie

def sumuj_do3(liczba):
    return sum((liczba for liczba in range(1, liczba + 1)))     # lista

def sumuj_do4(liczba):
    return sum({liczba for liczba in range(1, liczba + 1)})     # zbiór

# ciąg arytemtyczny

def sumuj_do5(liczba):
    return (1 + liczba)/2 * liczba

start = time.perf_counter()
print(sumuj_do(5))
end = time.perf_counter()
print(end - start)

print(sumuj_do2(6))
print(sumuj_do3(6))
print(sumuj_do4(6))
print(sumuj_do5(6))

# Suma wszystkich argumentow

def count(*arg):
    return sum(arg)

print(count(2, 4, 1, 2, 5, 4, 10))

# Obiekty muttable / immuttable

listSample = [1, 4, 512, 65]
listSample2 = listSample
listSample2.append(3332)
print(id(listSample))
print(id(listSample2))

a = 4
print(id(a))
b = a
print(id(b))
b = 7
print(id(b))