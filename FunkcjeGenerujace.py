def generate_even_numbers():
    for element in range(400):
        if element % 2 == 0:
            yield element


evenNumbersGenerator = (element
                        for element in range(400)
                        if element % 2 == 0)

a = generate_even_numbers()


def generate_10_numbers():
    liczba = 0
    while liczba < 10:
        yield liczba
        liczba = liczba + 1


liczby = generate_10_numbers()

# generator kolejnych liczb przemnozonych przez siebie


def number_multipled_by_itself_generator():
    number = 0
    while True:
        # number = number + 1
        number = yield number * number


generatedNumbers = []

numberGenerator = number_multipled_by_itself_generator()

numberGenerator.send(None)
# next(numberGenerator)

for i in range(20):
    generatedNumbers.append(numberGenerator.send(i))

print(generatedNumbers)
