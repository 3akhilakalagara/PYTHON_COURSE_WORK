from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass
    
class Foodorder(Order):
    def process_order(self):
        print("available food at restaurants")
    
class Groceryorder(Order):
    def process_order(self):
        print("available grocery items in the store")
        
class Medicineorder(Order):
    def process_order(self):
        print("available medicine in the medical store")

class Cloudkitchenorder(Order):
    def process_order(self):
        print("available items in the cloudkitchen")

class Petsuppliesorder(Order):
    def process_order(self):
        print("available pet items in the store")
        
class Meatorder(Order):
    def process_order(self):
        print("available quantity of meat in the store")

class Cakeorder(Order):
    def process_order(self):
        print("available flavours of cake in the bakery")

class Partyorder(Order):
    def process_order(self):
        print("items ordered for party tonight")
        
class Juiceorder(Order):
    def process_order(self):
        print("available fruit juices in the store")
    
def handle_order(order):
    order.process_order()
    
orders = [
    Foodorder(),
    Groceryorder(),
    Medicineorder(),
    Cloudkitchenorder(),
    Petsuppliesorder(),
    Meatorder(),
    Cakeorder(),
    Partyorder(),
    Juiceorder()
]

for order in orders:
    handle_order(order)