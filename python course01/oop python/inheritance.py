# base class parent class, common attrivute + fuctionality clss
# deriverd class, child class, uncommon attrivute + funcitonaity classs

class Laptop:
    def __init__(self,brand, price, color,orgin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.orgin = orgin
        
    def rum(self):        
        return f'Running laptop: {self.brand}'    
        
        
    class Laptop:
        def __init__(self, memory, ssd) -> None:
            self.memory = memory
            self.ssd = ssd
        
    
    def coding(self):
        return f'learning python and practicing'

class Phone:
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
               self.dual_sim = dual_sim     
               super().__init__(brand, price, color, origin)
  
    def phone_call(self, number, text):
       return f'sending SMS to: {number} with: [text]'
 
    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.price} {self.dual_sim}'
    
class Camera:
    def __init__(self, pixel) -> None:
           
        self.pixel = pixel
           
    def change_lens(self):
        pass
         
           
# inheritance
my_phone = Phone('iphon', 120000, 'sivler', 'china', True)
print(my_phone.brand)
print(my_phone)