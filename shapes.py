class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_surface_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, sideLength):
        #self.sideLength = sideLength
        super().__init__(sideLength, sideLength)

class Cube(Square):
    def count_surface_area(self):
        return super().count_surface_area() * 6

    def count_volume(self):
        return super().count_surface_area() * self.height


square = Square(3)

print(square.count_surface_area())

cube = Cube(5)

print(cube.count_surface_area())
print(cube.count_volume())
