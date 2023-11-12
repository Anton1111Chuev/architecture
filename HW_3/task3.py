"""3) Переписать код в соответствии с Interface Segregation Principle:
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius

    def volume(self):
        raise NotImplementedError("Circle does not have volume")

class Cube(Shape):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge """

from abc import ABCMeta, abstractmethod
import math


class Shape:
    __metaclass__: ABCMeta

    @abstractmethod
    def area(self):
        pass


class VolumeShape(Shape):
    __metaclass__: ABCMeta

    @abstractmethod
    def volume(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius


class Cube(VolumeShape):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge
