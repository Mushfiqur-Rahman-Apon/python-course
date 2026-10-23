class Shopping:
    cart = [] #class attribute  # static attrebute
    origin =  'china'
    
    def __init__(self, name, location) -> None:
        self.name = 'jamu na city' # instance attribuute
        self.location = 'jam er maj khane'
        
    def purchase(self, item, price, amount):
        premaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')
    
    def hudai_dekhi(self, item):
        print('hudai dekhi kintu inmu just ac er haw')
        
basundara = Shopping('vasu en dhara', 'not popular location')
basundara.purchase('lungi', 500, 1000)            
        
Shopping.purchase(2, 3, 3)        