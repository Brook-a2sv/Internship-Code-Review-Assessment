
import math


class CircleMeasurement:
    def __init__(self, radius):
        self.radius = radius

    # calculae circumference of a circle
    def CircleCircumference(self):
        return 2 * math.pi * self.radius
    
    # calculae area of a circle
    def CircleArea(radius):
        return 3.14 * radius ** 2

class Oprerations:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # dividing two numbers
    def divide_numbers(a, b):
        return a / b
    # we can add other operations here
