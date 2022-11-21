from Lotto import choose_numbers2


def test_choose_numbers2():
    actual = choose_numbers2(3, 49)

    assert actual == 123
