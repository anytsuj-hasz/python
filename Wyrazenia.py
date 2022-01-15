# Wyrazenie listowe

liczby = [1, 2, 3, 4, 5, 6, 7]

potegiDwojki =[
    element **2
    for element in liczby
    ]

liczbyParzyste =[
    element2
    for element2 in liczby
    if (element2 % 2 == 0)
    ]

print(potegiDwojki)
print(liczbyParzyste)

# Wyrazenia generyczne

evenNumbersGenerator = (
    number
    for number in range(50)
    if (number % 5 == 0)
    )
for item in evenNumbersGenerator:
    print(item)

# Wyrazenie slownikowe

names = {"Arek", "karol", "Olga", "michal"}

namesLength = {
    name : len(name)
    for name in names
    }

print(namesLength)

# Wyrazenie zbioru

names = {
    name.capitalize()
    for name in names
    }
print(names)

# Zadanie: znajdz liczby od 0 do 400 wlacznie, podzielne przez 7 ale nie podzielne przez 5

zbiorLiczb = [
    liczba
    for liczba in range(401)
    if (liczba % 7 == 0)
    if (liczba % 5 != 0)
    ]
print(zbiorLiczb)
