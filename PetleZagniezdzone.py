ListaGosci = [
    ('Anna', 28, 'kobieta', 123456),
    ('Jan', 32, 'mezczyzna', 564786),
    ('Tomasz', 27, 'mezczyzna', 987654),
    ('Iwona', 20, 'kobieta', 346791)
]

ListaGosci.append(('Ola', 19, 'kobieta', 777555))

for imie, wiek, plec, telefon in ListaGosci:
    print("Imie: ", imie)
    print("Wiek: ", wiek)
    print("Plec: ", plec)
    print("Telefon: ", telefon)
    print("\n")
