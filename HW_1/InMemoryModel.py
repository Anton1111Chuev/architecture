from abc import ABCMeta, abstractmethod


class IModelChangedObserver:
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply_update_model(self):
        pass


class IModelChanger:
    __metaclass__ = ABCMeta

    @abstractmethod
    def notify_change(self, sender: IModelChangedObserver):
        pass


class ModelStore(IModelChanger):

    def __init__(self, changed_observers: list[IModelChangedObserver]):
        self.models = []
        self.scenas = []
        self.flashes = []
        self.cameras = []
        self.changeObservers = changed_observers

    def get_scena(self, id):
        return self.scenas[id]

    def notify_change(self, sender: IModelChanger):
        pass
