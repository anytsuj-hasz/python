"""
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
"""
oceny = {
    "Arkadiusz": (2, 5, 3, 4, 3),
    "Anna": (3, 4, 2, 3)
}

for klucz in oceny:
    print(klucz, "oceny: ", oceny[klucz])

people = {
        "abcd1234": {'name': 'Jan', 'age': 27, 'sex': 'male'},
        "gfdt5678": {'name': 'Anna', 'age': 34, 'sex': 'female'},
        "trwf0987": {'name': 'Pawel', 'age': 30, 'sex': 'male'},
        "cbhg6537": {'name': 'Olga', 'age': 27, 'sex': 'female'}
        }

for id, dictionary in people.items():
    print("ID: ", id)
    for key in dictionary:
        print(key, ": ", dictionary[key])