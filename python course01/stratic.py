class Shopping:
    cart = [] #class attrivbute #static attribute
    origin = 'china'
    
    def __init__(self, name, location) -> None:
        self.name = 'jamu na city' # instance attribute
        self.location = 'jam er maj khane'
        
        
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')   
        
        
    basundara = Shopping
    # shopping .purchase(2, 3, 3)  