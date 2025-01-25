import math
from abc import ABC, abstractmethod

# Base class (Abstract class)
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

# Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height

# Circle class
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)

# Function to calculate the area
def calculate_area(polygon):
    print(f"The area of the {polygon.__class__.__name__} is: {polygon.area()}")

# Main code to test the classes
if __name__ == "__main__":
    # Create objects of different polygons
    rectangle = Rectangle(10, 5)
    triangle = Triangle(6, 4)
    circle = Circle(7)

    # Calculate and print the area of each polygon
    calculate_area(rectangle)
    calculate_area(triangle)
    calculate_area(circle)
