"""4) Переписать код в соответствии с Liskov Substitution Principle:
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def setWidth(self, width):
        self.width = width
        self.height = width

    def setHeight(self, height):
        self.width = height
        self.height = height"""

from abc import ABCMeta, abstractmethod


class Shape:
    __metaclass__: ABCMeta

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return self.side ** 2
