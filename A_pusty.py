class Zwierzeta():
    def __init__(self, rodzina, gatunek):
        self.gatunek = gatunek
        self.rodzina = rodzina

class Pies(Zwierzeta):

    gatunek = "Psowate"
    rodzina = "Eukarioty"

    def przedstawienie(self, imie):
        print("Nazywam się: " + imie + "Jestem psem z gatunku: " + self.gatunek + "i rodziny: " + self.rodzina)


Pies.mojPies = ("Burek")

wynik = Pies.przedstawienie(super)
