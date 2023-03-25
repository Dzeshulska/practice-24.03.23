class AutoPark :
    def __init__(self, label, manufacturer, price, category) :
        self._label = label
        self._manufacturer = manufacturer
        self._price = price
        self._category = category

    def getCategory(self) :
        return self._category
    

class Sedan(AutoPark) :
    def __init__(self, label, manufacturer, price, category, bibi) :
        super().__init__(self, label, manufacturer, price, category)
        self._bibi = bibi

class Truck(AutoPark) :
    def __init__(self, label, manufacturer, price, category, fafa) :
        super().__init__(self, label, manufacturer, price, category)
        self._fafa = fafa

class Hatchback(AutoPark) :
    def __init__(self, label, manufacturer, price, category, meep) :
        super().__init__(self, label, manufacturer, price, category)
        self._meep = meep


class AutoParkDB :
    products = {
        "Sedan" : [],
        "Truck" : [],
        "Hatchback" : []
    }

    