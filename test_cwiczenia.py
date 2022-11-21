import cwiczenia


def test_sumuj_liczby():
    actual = cwiczenia.sumuj_liczby(7, 5)
    assert actual == 12


def test_stworz_liste_min():
    lista = cwiczenia.stworz_liste()
    assert min(lista) == 1


def stworz_liste_max():
    lista = cwiczenia.stworz_liste()
    assert max(lista) == 10


def stworz_liste_dlugosc():
    lista = cwiczenia.stworz_liste()
    assert len(lista) == 10


def test_pomnoz_liczby():
    actual = cwiczenia.pomnoz_liczby(2, 8)
    assert actual == 16
