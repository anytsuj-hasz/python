import requests
import json
from credentials import headers

def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Nieprawidlowy format", response.text)
    else:
        return content

def get_favourite_cats(userId):
    params = {
        "sub_id": userId
    }
    r = requests.get('https://api.thecatapi.com/v1/favourites/', params, headers=headers)
    return get_json_content_from_response(r)

def get_random_cat():
    r = requests.get("https://api.thecatapi.com/v1/images/search", headers=headers)
    return get_json_content_from_response(r)[0]

def add_favourite_cat(catId, userId):
    catData = {
        "image_id": catId,
        "sub_id": userId
    }
    r = requests.post("https://api.thecatapi.com/v1/favourites", json=catData, headers=headers)
    return get_json_content_from_response(r)

def remove_favourite_cat(userId, favouriteCatId):
    r = requests.delete("https://api.thecatapi.com/v1/favourites/"+favouriteCatId, headers=headers)
    return get_json_content_from_response(r)

print("Hej, zaloguj się - podaj login i haslo")
#pobieramy login i hasło, sprawdzamy czy sa one poprawne, logujemy się
#pobieramy z bazy danych userID i name

userId = "agh2m"
name = "Arkadiusz"

print("Witaj" + name)
favouriteCats = get_favourite_cats(userId)
print("Twoje ulubione kotki to: ", favouriteCats)
randomCat = get_random_cat()
print("Wylosowano kotka: ", randomCat["url"])

addToFavourites = input("Czy chcesz dodac tego kotka do ulubionych? T/N ")
newlyAddedCatInfo = {}
if addToFavourites.upper() == "T":
    resultFromAddingFavouriteCat = add_favourite_cat(randomCat["id"], userId)
    newlyAddedCatInfo = {resultFromAddingFavouriteCat["id"]: randomCat["url"]}
else:
    print("Kot nie zostal dodany do ulubionych")

favouriteCatsById = {
    favouriteCat["id"]: favouriteCat["image"]["url"]
    for favouriteCat in favouriteCats
}
favouriteCatsById.update(newlyAddedCatInfo)

print(favouriteCatsById)

favouriteCatId = input("Czy chcesz usunac kota z ulubionych? Podaj ID: ")
print(remove_favourite_cat(userId, favouriteCatId))