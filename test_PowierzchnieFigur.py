from PowierzchnieFigur import poleProstokata
from PowierzchnieFigur import poleKwadratu
from PowierzchnieFigur import poleTrojkata


def test_pole_prostokata():
    # given
    bokA = 2
    bokB = 3

    # when
    actual = poleProstokata(bokA, bokB)

    # then
    assert actual == 6


def test_pole_kwadratu():
    bokA = 4
    actual = poleKwadratu(bokA)
    assert actual == 16


def test_pole_trojkata():
    podstawa = 4
    wysokosc = 3
    actual = poleTrojkata(podstawa, wysokosc)
    assert actual == 6
