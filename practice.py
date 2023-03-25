class Store:
    def __init__(self,manufacturer,label,price,date):
        self.manufacturer = manufacturer
        self.label = label
        self.price = price
        self.date = date
    
    
    def getLabel (self) :
        print(self._label)

    def getPrice (self) :
        print(self._price)


class User:
    def __init__(self,role,name,money,bag):
        self.role = role
        self.name = name
        self.money = money
        self.bag = bag
    
class Cart:
    def __init__(self,card_number,card_date,card_cvv):
        self.card_number = card_number
        self.card_date = card_date
        self.card_cvv = card_cvv
     

class Admin(User):
    """характеристика админа"""
    def __init__(self,role,product,price):
        super().__init__(self.role)
        self.produc = product
        self.price = price
Admin1 = Admin("administrator")
print(Admin1.role)