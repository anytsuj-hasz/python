# Szukamy użytkownika z największą ilością wykonanych tasków z listy todos

import requests
import json
from collections import defaultdict

r = requests.get("https://jsonplaceholder.typicode.com/todos")


def count_tasks_frequency(tasks):
    completedTasksFrequencyByUser = defaultdict(int)
    for entry in tasks:
        if (entry["completed"] == True):
            completedTasksFrequencyByUser[entry["userId"]] += 1
    return completedTasksFrequencyByUser


def users_with_top_max_tasks(completedTasksFrequencyByUser):
    usersIdWithMaxCompletedTasks = []
    maxAmountOfCompletedTasks = max(completedTasksFrequencyByUser.values())
    for userId, numberOfCompletedTasks in completedTasksFrequencyByUser.items():
        if numberOfCompletedTasks == maxAmountOfCompletedTasks:
            usersIdWithMaxCompletedTasks.append(userId)
    return usersIdWithMaxCompletedTasks


try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTasksFrequencyByUser = count_tasks_frequency(tasks)
    usersIdWithTopOfMaxCompletedTasks = users_with_top_max_tasks(completedTasksFrequencyByUser)


def change_list_into_conj_of_param(my_list, key="id"):
    conjParam = key + "="
    lasIteration = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lasIteration):
            conjParam += str(item)
        else:
            conjParam += str(item) + "&" + key + "="

    return conjParam


conjParam = change_list_into_conj_of_param(usersIdWithTopOfMaxCompletedTasks)
r = requests.get("https://jsonplaceholder.typicode.com/users", params=conjParam)

users = r.json()

for user in users:
    print("Wreczamy ciasteczko za najwieksza ilosc wykonanych taskow: ", user["name"])