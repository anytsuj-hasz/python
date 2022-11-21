def generate_even_numbers():
    for element in range(400):
        if element % 2 == 0:
            yield element


evenNumbersGenerator = (element
                        for element in range(400)
                        if element % 2 == 0)

a = generate_even_numbers()

#wywolanie: next(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

def generate_10_numbers():
    liczba = 0
    while liczba < 10:
        yield liczba
        liczba = liczba + 1


print(list(generate_10_numbers()))


# generator kolejnych liczb przemnozonych przez siebie


def number_multipled_by_itself_generator():
    number = 0
    while True:
        # number = number + 1
        number = yield number * number


generatedNumbers = []

numberGenerator = number_multipled_by_itself_generator()

numberGenerator.send(None)

for i in range(20):
    generatedNumbers.append(numberGenerator.send(i+5))


print(generatedNumbers)


def odd_numbers_generator():
    number = 0
    while True:
        if number % 3 == 0:
            yield number
        number = number + 1


odd_numbers_generator_instance = odd_numbers_generator()
# for index in range(30):
#     next(odd_numbers_generator_instance)

for index in range(30):
    print(next(odd_numbers_generator_instance))
