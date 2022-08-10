# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Shape:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def square(self,a=0,b=0):
        return a * b
    def perimeter(self, a, b):
        return 0

class Rectanlge(Shape):
    def print():
        return ''

class Square(Shape):
    def square(self):
        return self.a ** 2

    def perimeter(self,a, b=0):
        return a * 4

class Triangle(Shape):
    def square(self,a=0, b=0):
        return a * b / 2



rectangle = Rectanlge()
square = Square(5,6)
triangle = Triangle()
print(rectangle.square(5))
print(square.square())
print(triangle.square(5,6))

print(rectangle.perimeter(5,6))
print(square.perimeter(5,6))
print(triangle.perimeter(5,6))
