import requests
import json
import webbrowser

choice = input("Choose cat or dog to display 5 facts: ")

params = {
    "animal_type": "dog"
}

if (choice == "cat"):
    try:
        rCat = requests.get("https://cat-fact.herokuapp.com/facts/random?amount=5")
        content = rCat.json()
    except json.decoder.JSONDecodeError:
        print("Invalid format")
    else:
        for cat in content:
            print(cat["text"])
elif (choice == "dog"):
    try:
        rDog = requests.get("https://cat-fact.herokuapp.com/facts/random?amount=5", params)
        content = rDog.json()
    except json.decoder.JSONDecodeError:
        print("Invalid format")
    else:
        for dog in content:
            print(dog["text"])
else:
    print("You choosed wrong animal type")

# Open 3 pictures of cat: American curl (acur)

r = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=acur&limit=3")

try:
    cats = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format")
else:
    for cat in cats:
        webbrowser.open_new_tab(cat["url"])
