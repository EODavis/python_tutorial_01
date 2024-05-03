# This is a sample Python script.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self, ):
        return self.width * self.height

    def perimeter(self, ):
        return 2 * (self.width + self.height)

    def __add__(self, other):
        return self.width + other.width, self.height + other.height


rec1 = Shape(5, 8)
rec2 = Shape(2, 7)

print(rec1.area())
print(rec2.perimeter())
new = rec1 + rec2
print(new)
