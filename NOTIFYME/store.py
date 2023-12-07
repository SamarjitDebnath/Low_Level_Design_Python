from observable.iphoneObservable import IphoneStockObservable
from observer.emailAlertObserver import EmailAlertObserver
from observer.mobileAlertObserver import MobileAlertObserver

if __name__ == '__main__':
    iphoneItem = IphoneStockObservable()

    emailUser1 = EmailAlertObserver("random_mail1@example.com", iphoneItem)
    emailUser2 = EmailAlertObserver("random_mail2@example.com", iphoneItem)
    emailUser3 = EmailAlertObserver("random_mail3@example.com", iphoneItem)
    emailUser4 = EmailAlertObserver("random_mail4@example.com", iphoneItem)
    mobileUser1 = MobileAlertObserver("random_id001", iphoneItem)

    iphoneItem.addUser(emailUser1)
    iphoneItem.addUser(emailUser2)
    iphoneItem.addUser(emailUser3)
    iphoneItem.addUser(emailUser4)
    iphoneItem.addUser(mobileUser1)

    print(iphoneItem.get_stockCount())
    iphoneItem.addStock(10)
    print(iphoneItem.get_stockCount())
    iphoneItem.addStock(100)
    print(iphoneItem.get_stockCount())
    iphoneItem.removeStock(50)
    print(iphoneItem.get_stockCount())
    iphoneItem.removeStock(60)
    print(iphoneItem.get_stockCount())
    iphoneItem.addStock(1)
    print(iphoneItem.get_stockCount())
