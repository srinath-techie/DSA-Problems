class PurchaseSystem:
    def __init__(self):
        self.products = {'apple': 2, 'banana': 1, 'orange': 3}
        self.cart = []
    
    def add_to_cart(self, product, quantity): 
        if product in self.products: self.cart.append((product, quantity))
    
    def total_price(self): 
        return sum(self.products[product] * quantity for product, quantity in self.cart)
    
    def view_cart(self): 
        for product, quantity in self.cart: print(f"{product} x{quantity} = {self.products[product] * quantity}")

purchase_system = PurchaseSystem()
purchase_system.add_to_cart('apple', 3)
purchase_system.add_to_cart('banana', 2)
purchase_system.view_cart()
print("Total Price:", purchase_system.total_price())
