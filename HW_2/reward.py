from abc import ABC, abstractmethod
from random import randint


class IGameItem(ABC):

    def open(self):
        print(type(self).__name__)


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


class Gold(IGameItem):
    pass


class Gem(IGameItem):
    pass


class Silver(IGameItem):
    pass


class Ruby(IGameItem):
    pass


class Coin(IGameItem):
    pass


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()


class SilverGenerator(ItemFabric):
    def create_item(self):
        return Silver()


class RubyGenerator(ItemFabric):
    def create_item(self):
        return Ruby()


class CoinGenerator(ItemFabric):
    def create_item(self):
        return Coin()


if __name__ == '__main__':
    rewards = [GoldGenerator(), GemGenerator(), SilverGenerator(), RubyGenerator(), CoinGenerator()]

    for i in range(20):
        rewards[randint(0, 4)].create_item().open()
