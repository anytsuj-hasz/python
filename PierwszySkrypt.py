# Powitanie

imie = str(input("Podaj swoje imie: "))

print("Hej, witaj ", imie)

wiek = int(input("Wpisz, ile masz lat: "))

print("Bardzo fajnie, za rok bedziesz miec: ", wiek + 1, " lat!")


# Instrukcja warunkowa - kalkulator

wybor = input("* - mnozenie, / - dzielenie, + - dodawanie, - - odejmowanie")

a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

if wybor == "*":
    print(a * b)
elif wybor == "/":
    if (b == 0):
        print("Nie dziel przez zero!")
    else:
        print(a / b)
elif wybor == "+":
    print(a + b)
elif wybor == "-":
    print(a - b)
else:
    print("Nie dokonales wyboru.")
