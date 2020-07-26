class product:
    deliveryCharge=50
    def __init__(self,nam, prc):
        self.name=nam
        self.price=prc
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price + product.deliveryCharge
        
class gift(product):
    wrappingCharge=100
    def __init__(self, nam, prc):
        super().__init__(nam, prc)
    def get_price(self):
        return self.price + product.deliveryCharge + gift.wrappingCharge

p1 = product("Toy-car", 1500)
print("The {} will cost you Rs.{}.".format(p1.get_name(),p1.get_price()))
g1 = gift("Toy-car", 1500)
print("The {} will cost you Rs.{}.".format(g1.get_name(),g1.get_price()))        
