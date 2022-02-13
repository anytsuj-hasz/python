class User:   

    def __init__(self, age, name):
        self.age = age
        self.name = name


    def print_age(self, message):
        print("wiek: ", self.age, self.name, message)


user1 = User(13, "Ola")
user2 = User(25, "Maciek")

user1.print_age("dodatkowy komentarz")
user2.print_age("")
