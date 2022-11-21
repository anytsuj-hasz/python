from datetime import datetime

def measure_time(func):
    def wew(*args, **kwargs):
        print("start: ", datetime.now())
        result = func(*args, **kwargs)
        print("end: ", datetime.now())
        return result
    return wew


@measure_time
def sumuj_liczby(a, b):
    return a + b


@measure_time
def pomnoz_liczby(a, b):
    return a * b


def stworz_liste():
    return list(range(1, 11))


suma = sumuj_liczby(17, 938)
print(suma)
iloczyn = pomnoz_liczby(2, 6)
print(iloczyn)
iloczyn2 = pomnoz_liczby(67, 489)
print(iloczyn2)



# kiedy fukncja wywołuje samą siebie (rekursja) - dekorator mierzenia czasu pokazuje czas dla każdego wywołania, liczy też czas wykonywania samego dekoratora

"""def silnia(n):
    if n > 1:
        return n * silnia(n-1)
    return 1


@measure_time
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


liczba = int(input("Podaj liczbę: "))

wynikSilnia = silnia(liczba)
wynikFib = fibonacci(liczba)
print("Silnia dla liczby ", liczba, " wynosi: ", wynikSilnia)
print("Fibonacci dla liczby ", liczba, " wynosi: ", wynikFib)
"""



