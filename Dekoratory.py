def dekorator1(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper


@dekorator1
@dekorator1
def hello_world():
    print("Hello world")

def hello_world_simple():
    print("Hello world")

hello_world()
dekorator1(dekorator1(hello_world_simple))()
