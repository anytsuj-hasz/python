class User:
    id = 0

    def __init__(self, name=""):
        self.name = name
        User.id +=1
        self.id = User.id

    