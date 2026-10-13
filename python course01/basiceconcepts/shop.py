class Shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)


mehbeeeen = Shop('meh jabeeeen')
mehbeeeen.add_to_cart('shoes')
mehbeeeen.add_to_cart('phone')
print(mehbeeeen.cart)

nisho = Shop('noisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)