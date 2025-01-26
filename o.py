import math

# Base class Polygon
class Polygon:
    def area(self):
        pass

# Rectangle class (inherits from Polygon)
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Circle class (inherits from Polygon)
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

# Triangle class (inherits from Polygon)
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Square class (inherits from Rectangle)
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# Main program
def main():
    # Create objects of different polygons
    rectangle = Rectangle(5, 10)
    circle = Circle(7)
    triangle = Triangle(8, 4)
    square = Square(6)

    # Display the areas
    print(f"Area of Rectangle: {rectangle.area()}")
    print(f"Area of Circle: {circle.area()}")
    print(f"Area of Triangle: {triangle.area()}")
    print(f"Area of Square: {square.area()}")

if __name__ == "__main__":
    main()
