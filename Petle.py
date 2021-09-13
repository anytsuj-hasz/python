# Pętla while (suma 4 liczb podanych przez użytkownika)

print("*** z użyciem pętli while")
wynik = 0

i = 0
while i < 4:
    x = int(input("Podaj liczbę: "))
    wynik += x
    i += 1

print("Wynik dodawania 4 liczb to: ", wynik)

print("*** z użyciem pętli for")
wynik2 = 0

for i in range(0, 4):
    x = int(input("Podaj liczbę: "))
    wynik2 += x

print("Wynik dodawania to: ", wynik2)

# Wypisuje liczby od 0 do 200, podzielne przez 5 i niepodzielne przez 7

for i in range(0, 201):
    if (i % 5 == 0 and not(i % 7 == 0) ):
        print(i)

# Suma dodawania trzech dodatnich, parzystych liczb

wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj dodatnia liczbe parzysta: "))
    if (x % 2 == 0 and x > 0):
        wynik += x
    else:
        print("Nie podales dodatniej liczby parzystej, podaj jeszcze raz: ")
        continue
    i += 1
print("Wynik dodawania to: ", wynik)
