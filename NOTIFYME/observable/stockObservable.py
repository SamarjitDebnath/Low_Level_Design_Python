from abc import ABC, abstractmethod


class StockObservable(ABC):

    @abstractmethod
    def addUser(self, observer):
        pass

    @abstractmethod
    def removeUser(self, observer):
        pass

    @abstractmethod
    def notifySubscribers(self):
        pass

    @abstractmethod
    def set_stockCount(self, newStockCount):
        pass

    @abstractmethod
    def get_stockCount(self):
        pass

    @abstractmethod
    def addStock(self, newStockCount):
        pass

    @abstractmethod
    def removeStock(self, newStockCount):
        pass
