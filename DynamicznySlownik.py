definicje = {}

while True:

    print("1: Dodaj definicje")
    print("2: Znajdz definicje")
    print("3: Usun definicje")
    print("4: Zakoncz")

    wybor = input("Co chcesz zrobic? Wprowadz 1, 2, 3 lub 4: ")

    if wybor == "1":
        klucz = input("Podaj haslo (slowo) do zdefiniowania: ")
        definicja = input("Podaj definicje: ")
        definicje[klucz] = definicja
        print("Definicja zostala dodana pomyslnie \n")
    elif wybor == "2":
        klucz = input("Podaj haslo: ")
        if klucz in definicje:
            print(definicje[klucz], "\n")
        else:
            print("Podanego hasla: ", klucz, " nie ma w slowniku \n")
    elif wybor == "3":
        klucz = input("Jaka definicje chcesz usunac: ")
        if klucz in definicje:
            del definicje[klucz]
            print("Definicja zostala usunieta \n")
        else:
            print("Brak hasla: ", klucz, " do usuniecia \n" )
    elif wybor == "4":
        print("Zamykamy slownik")
        break
    else:
        print("Nie wybrales prawidlowej wartosci, podaj jeszcze raz \n")
        