from observer.notificationAlertObserver import NotificationAlertObserver
from observable.stockObservable import StockObservable


class MobileAlertObserver(NotificationAlertObserver):

    def __init__(self, _userId: str, observable: StockObservable):
        self._userId = _userId
        self._observable = observable

    def update(self):
        self.sendMobileAlert(self._userId, "Product is in stock, hurry up!!!")

    def sendMobileAlert(self, userId: str, message: str):
        print(f"message sent to {userId}\nmessage: {message}")
