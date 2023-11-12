"""5) Переписать код в соответствии с Dependency Inversion Principle:
class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

class PetrolEngine:
    def start(self):
        pass"""

from abc import ABCMeta, abstractmethod


class Engine:
    __metaclass__: ABCMeta

    @abstractmethod
    def start(self):
        pass


class PetrolEngine:
    def start(self):
        pass


class DieselEngine:
    def start(self):
        pass


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine
