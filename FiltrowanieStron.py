import requests
from requests.exceptions import RequestException


def is_valid(address):
    try:
        response = requests.get(address)
        if response.status_code == 200:
            return True
        else:
            return False
    except RequestException:
        return False


def read_file(fileName):
    with open(fileName, "r") as inputFile:
        addressLines = inputFile.read().splitlines()
        return addressLines


def save_file(lines):
    fileName = (input("Podaj nazwę pliku:"))
    with open(fileName, "w") as file:
        for line in lines:
            file.write(line + "\n")


def get_valid_addresses(addressLines):
    validAddresses = []
    for address in addressLines:
        if is_valid(address):
            validAddresses.append(address)
    return validAddresses


addresses = read_file("plik.txt")
validAdresses = get_valid_addresses(addresses)
save_file(validAdresses)

'''
Spróbuj jako trening umieścić ostatnią część kodu również w funkcji, a najlepiej w trzech :)
1) Jedna odpowiadająca za zapis 'poprawnych danych' do pliku  (podanego przez użytkownika),
2) druga za otwarcie pliku ze wszystkimi danymi
3) za cały proces walidacji (linia 19-21)

with open("plik.txt", "r") as inputFile:
    with open("validSites.txt", "w") as resultsFile:
        addressLines = inputFile.read().splitlines()
        for address in addressLines:
            if is_valid(address):
                resultsFile.write(address + "\n")
'''

