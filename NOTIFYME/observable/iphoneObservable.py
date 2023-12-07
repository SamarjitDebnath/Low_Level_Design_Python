from typing import List
from observable.stockObservable import StockObservable
from observer.notificationAlertObserver import NotificationAlertObserver


class IphoneStockObservable(StockObservable):
    _observerList: List[NotificationAlertObserver] = []
    _stockCount: int = 0

    def addUser(self, observer: NotificationAlertObserver):
        self._observerList.append(observer)

    def removeUser(self, observer: NotificationAlertObserver):
        self._observerList.remove(observer)

    def notifySubscribers(self):
        for observer in self._observerList:
            observer.update()

    def set_stockCount(self, stockCount: int):
        self._stockCount = stockCount

    def get_stockCount(self):
        return self._stockCount

    def addStock(self, newStockCount: int):
        if self._stockCount == 0:
            self.notifySubscribers()
        newStockCount = self._stockCount + newStockCount
        self.set_stockCount(newStockCount)

    def removeStock(self, newStockCount: int):
        newStockCount = self._stockCount - newStockCount
        newStockCount = newStockCount if newStockCount >= 0 else 0
        self.set_stockCount(newStockCount)
