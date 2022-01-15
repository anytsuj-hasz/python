class User:
    age = 0
    name = ""

    def print_age(self, message):
        print("wiek: ", self.age, self.name, message)

user1 = User()
user2 = User()

user1.age = 26
user1.name = "Arek"
user1.print_age("dodatkowy komentarz")

user2.age = 42
user2.name = "Anna"
user2.print_age("")