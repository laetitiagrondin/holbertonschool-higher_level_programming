#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return height * width

    def perimeter():
        return 2 *(height + width)

def shape_info():
    print(f"Area: {shape.area()}")
    print(f"Area: {shape.area()}")
