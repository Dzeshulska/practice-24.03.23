class Store:
    def__init__(self,manufacturer,label,price,date):
        self.manufacturer = manufacturer
        self.label = label
        self.price = price
        self.date = date
    
    
    def getLabel (self) :
        print(self._label)

    def getPrice (self) :
        print(self._price)


class User:
    def__init__(self,name,money,bag):
        self.name = name
        self.money = money
        self.bag = bag
    
class Cart:
    def__init__(self,card_number,card_date,card_cvv):
        self.card_number = card_number
        self.card_date = card_date
        self.card_cvv = card_cvv
     

class Admin:
    def__init__(self,role,product,price):
        self.role = role
        self.produc = product
        self.price = price