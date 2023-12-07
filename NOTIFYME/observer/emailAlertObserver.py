from typing import List
from observer.notificationAlertObserver import NotificationAlertObserver
from observable.stockObservable import StockObservable


class EmailAlertObserver(NotificationAlertObserver):

    def __init__(self, emailId: str, observable: StockObservable):
        self._emailId = emailId
        self._observable = observable

    def update(self):
        self.sendEmail(self._emailId, "Product is in stock, hurry up!!!")

    def sendEmail(self, emailId: str, message: str):
        print(f"mail sent to {emailId}\nmessage: {message}")
